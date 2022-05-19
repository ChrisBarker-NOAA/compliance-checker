#!/usr/bin/env python
# -*- coding: utf-8 -*-

from compliance_checker import cfutil
from compliance_checker.base import BaseCheck, BaseNCCheck, Result, TestCtx
from compliance_checker.cf import util
from compliance_checker.cf.appendix_d import (
    dimless_vertical_coordinates_1_6,
    dimless_vertical_coordinates_1_7,
    no_missing_terms
)

from compliance_checker.cf.appendix_e import cell_methods16, cell_methods17
from compliance_checker.cf.appendix_f import (
    ellipsoid_names17,
    grid_mapping_attr_types16,
    grid_mapping_attr_types17,
    grid_mapping_dict16,
    grid_mapping_dict17,
    horizontal_datum_names17,
    prime_meridian_names17
)

# Version specific checkers organized in other modules
from compliance_checker.cf.cf_1_6 import CF1_6Check
from compliance_checker.cf.cf_1_7 import CF1_7Check
from compliance_checker.cf.cf_1_8 import CF1_8Check
