# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Business Requirement Type",
    "version": "8.0.1.0.0",
    "category": "Business Requirements Management",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "business_requirement",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/business_requirement_type_views.xml",
        "views/business_requirement_views.xml",
    ],
}
