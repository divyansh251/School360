{
    "name": "School Management",
    "version": "1.0",
    "summary": "Manage teachers, students, and staff in a school",
    "category": "Education",
    "author": "Divyansh",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/sm_school_info_views.xml",
        "views/sm_class_info_views.xml",
        "views/sm_action_items.xml",
        "views/sm_menu_items.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False
}

