"""
_author_ = Johnleonard C.O
_Created_ =  12/5/2019
"""

import psycopg2
import os
import pandas as pd
import requests
import json


def close_con(con_cursor, con_connection):
	con_cursor.close()
	con_connection.close()
	print("PostgreSQL connection is closed")


def manage_connection():
	pg_user = os.getenv('PGUSER') or 'postgres'
	pg_password = os.getenv('PGPASSWORD') or '****'
	pg_host = os.getenv('PGHOST') or 'localhost'
	pg_port = os.getenv('PGPORT') or 5432
	db_name = 'risky_stuff'
	schema = 'data_raw'
	con = psycopg2.connect(user=pg_user, password=pg_password, host=pg_host, port=pg_port, database=db_name)
	main_cursor = con.cursor()
	return con, main_cursor, schema


def cursor_execute(cursor, query):
	cursor.execute(query)  # Execute the query
	result = cursor.fetchall()  # Fetch many
	df = pd.DataFrame(result)
	df = df.rename(columns={0: "buyerborrower1name", 1: "resaleflag", 2: "saleamt", 3: "saledate", 4: "propertyid", 5: "situsfullstreetaddress",
	                        6: "street_name", 7: "state", 8: "situsunittype", 9: "situsunitnbr", 10: "deed_city", 11: "sumresidentialunits",
	                        12: "nr_buildings", 13: "sumcommercialunits", 14: "geophy_gross_resid_building_area", 15: "sumlivingareasqft",
	                        16: "bedrooms", 17: "totalrooms", 18: "construction_year", 19: "effective_year_built", 20: "storiesnbrcode",
	                        21: "geophy_full_bathrooms", 22: "geophy_parcel_size_sqft", 23: "geom", 24: "geohash7", 25: "situslongitude",
	                        26: "situslatitude", 27: "assdtotalvalue", 28: "asslandvalue", 29: "assdimprovementvalue", 30: "propertyid_agg",
	                        31: "fatransactionid", 32: "geom_parcel", 33: "nr_floors"})
	print(df)
	return df


def geocode_address(street_name):
	lng = None
	lat = None
	key = os.getenv('GEO_API_KEY')
	r = requests.get(f"http://api.geocod.io/v1.4/geocode?q={street_name}&api_key={key}")
	r = json.loads(r.content)['results'][0]
	if r['accuracy'] < 0.8:
		raise NotImplemented
	else:
		lng = str(r['location']['lng'])
		lat = str(r['location']['lat'])
	return lat, lng


def search_data(cursor, street_name, city, net_floor_area, nr_units, sqft_price, construction_year, buildingarea, radio, lat, lng):
	if radio == 1:
		q = f"""
			select *
			from annual_deemtg_parcel
			where (sumresidentialunits::float > 0)
				and (geophy_gross_resid_building_area::float > 0)
				and (sumlivingareasqft::float > 0)

				and sumresidentialunits::float between {float(nr_units) - 2} and {float(nr_units) + 2}
				and geophy_gross_resid_building_area::float between {float(buildingarea) - 20} and {float(buildingarea) + 20}
				and street_name::text ilike '{street_name}%'
				and deed_city ilike '%{city}'
				and sumlivingareasqft::float between {float(net_floor_area) - 20} and {float(net_floor_area) + 20}
				and round(abs(saleamt::float/geophy_gross_resid_building_area::float)) between {float(sqft_price) - 10} and {float(sqft_price) + 10}
				and construction_year::int between {int(construction_year) - 1} and {int(construction_year) + 1}

			order by sumresidentialunits, geophy_gross_resid_building_area, sumlivingareasqft
			limit 15;
			"""

		print(q)
		return cursor_execute(cursor, q)
	elif radio == 2:
		q = f"""
			select *
			from annual_deemtg_parcel
			where (sumresidentialunits::float > 0)
				and (geophy_gross_resid_building_area::float > 0)
				and (sumlivingareasqft::float > 0)
				and sumresidentialunits::float between {float(nr_units) - 2} and {float(nr_units) + 2}
				and geophy_gross_resid_building_area::float between {float(buildingarea) - 20} and {float(buildingarea) + 20}
				and deed_city ilike '%{city}'
				and sumlivingareasqft::float between {float(net_floor_area) - 20} and {float(net_floor_area) + 20}
				and round(abs(saleamt::float/geophy_gross_resid_building_area::float)) between {float(sqft_price) - 10} and {float(sqft_price) + 10}
				and construction_year::int between {int(construction_year) - 1} and {int(construction_year) + 1}
	
			order by sumresidentialunits, geophy_gross_resid_building_area, sumlivingareasqft
			limit 15;
			"""

		print(q)
		return cursor_execute(cursor, q)
	elif radio == 3:
		q = f"""
			select *
			from annual_deemtg_parcel
			where (sumresidentialunits::float > 0)
				and (geophy_gross_resid_building_area::float > 0)
				and (sumlivingareasqft::float > 0)
				and sumresidentialunits::float between {float(nr_units) - 2} and {float(nr_units) + 2}
				and geophy_gross_resid_building_area::float between {float(buildingarea) - 20} and {float(buildingarea) + 20}
				and street_name::text ilike '{street_name}%'
				and deed_city ilike '%{city}'
				and round(abs(saleamt::float/geophy_gross_resid_building_area::float)) between {float(sqft_price) - 10} and {float(sqft_price) + 10}
				and construction_year::int between {int(construction_year) - 1} and {int(construction_year) + 1}

			order by sumresidentialunits, geophy_gross_resid_building_area, sumlivingareasqft
			limit 15;
			"""

		print(q)
		return cursor_execute(cursor, q)

	elif radio == 4:
		q = f"""
			select *
			from annual_deemtg_parcel
			where (sumresidentialunits::float > 0)
				and (geophy_gross_resid_building_area::float > 0)
				and (sumlivingareasqft::float > 0)
				and sumresidentialunits::float between {float(nr_units) - 2} and {float(nr_units) + 2}
				and geophy_gross_resid_building_area::float between {float(buildingarea) - 20} and {float(buildingarea) + 20}
				and deed_city ilike '%{city}'
				and round(abs(saleamt::float/geophy_gross_resid_building_area::float)) between {float(sqft_price) - 10} and {float(sqft_price) + 10}
				and construction_year::int between {int(construction_year) - 1} and {int(construction_year) + 1}

			order by sumresidentialunits, geophy_gross_resid_building_area, sumlivingareasqft
			limit 15;
			"""

		print(q)
		return cursor_execute(cursor, q)


def open_connection(street_name, city, net_floor_area, nr_units, sqft_price, construction_year, buildingarea, radio):
	try:
		connection, cursor, schema = manage_connection()
		if connection:
			print("\n ------------------------------------- Connection opened for --------------------------------------------------- \n")
			print(connection.get_dsn_parameters(), "\n")

			# Operation starts now
			# -----------------------------------------------------------------------------------------------------------
			cursor.execute("SET search_path TO firstamerican")
			lat, lng = geocode_address(street_name)
			return search_data(
				cursor,
				street_name,
				city,
				net_floor_area,
				nr_units,
				sqft_price,
				construction_year,
				buildingarea,
				radio,
				lat,
				lng,
			)

		close_con(cursor, connection)

	except psycopg2.DatabaseError as db_error:
		print("Error while connecting to PostgreSQL ", db_error)
