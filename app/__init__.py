from flask import Flask

from .counties import counties
from .extensions import db, migrate
from .model import connect_to_db, db, County, District, Group, DistrictGroup

def create_app(config_object='app.config.DevelopmentConfig'):
  app = Flask(__name__, instance_relative_config=False)
  app.config.from_object(config_object)
  app.jinja_env.undefined = StrictUndefined

  # Initialize extensions
  db.init_app(app)
  migrate.init_app(app, db)

  return app
  
@app.route('/')
def index():
    """Show homepage"""

    return render_template("homepage.html")


@app.route('/counties.json')
def county_info_json():
  """JSON information about counties"""

  counties = {
      county.county_id: {
      "county_name": county.county_name,
      "latitude": county.latitude,
      "longitude": county.longitude,
      "county_name_lower": county.county_name_lower
      }
      for county in County.query.limit(36)}

  return jsonify(counties)

@app.route('/statewide/<state>')
def statewide_statistics():
  """Show charts for statewide statistics"""

  return render_template("statewide.html", state=state)

@app.route('/county/<state>/<county>')
def county_stats():
  """Show statistics for a County"""
  assert (state in counties) and (county in counties['state'])
  return render_template("county.html", state=state, county=county)


if __name__ == "__main__":
  # app.debug = True
  connect_to_db(app)
  DebugToolbarExtension(app)
  app.run(host='0.0.0.0', port=5000)
