db.define_table("deployment_deployment",
                Field("need_type",
                      requires = IS_IN_SET(["Emergency", "Prepardness"])),
                Field("purpose", "text"),	
                Field("start_date", "date"),
                Field("end_date", "date"),
                Field("site_url"),
                Field("site_owner"),
                Field("organisation_contact_info", "text"),
                s3db.gis_location_id(),
                *s3_meta_fields())
