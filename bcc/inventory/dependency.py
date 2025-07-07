from django.core.cache import cache
import pandas as pd
from .services import get_all_rows

### Independent Global Variables
# Payment / Rates
banks = [
    'BDO', 'BPI', 'MetroBank'
]
all_locations = [
    'Armada', 'Legacy', 'Main', 'Premiere'
]
cc_discount_rates = [
    ('BDO Striaght', 0.0325),
    ('BDO 3mos', 0.04),
    ('BDO 6mos', 0.065),
    ('BDO 12mos', 0.125),
    ('BDO 24mos', 0.0),
    ('BPI Striaght', 0.042),
    ('BPI 3mos', 0.0),
    ('BPI 6mos', 0.065),
    ('BPI 12mos', 0.0),
    ('BPI 24mos', 0.0),
    ('MetroBank Striaght', 0.035),
    ('MetroBank 3mos', 0.035),
    ('MetroBank 6mos', 0.065),
    ('MetroBank 12mos', 0.105),
    ('MetroBank 24mos', 0.0),
]
dc_discount_rates = [
    ('BDO', 0.02),
    ('BPI', 0.03),
    ('MetroBank', 0.0),
]
cc_rate_dict = dict(cc_discount_rates)
dc_rate_dict = dict(dc_discount_rates)
bdo_online_discount_rate = 0.04

# Transaction Details
payment_method_choices = [
    'Cash',
    'GCash',
    'Bank Transfer',
    'Cheque',
    'Credit Card',
    'Debit Card',
    'BDO Checkout',
    'Receivables',
    'Payables',
]
suppliers = [
    'RC',
    'ENT',
    'SP',
    'YHI',
    'PWG',
]
inventory_movement = [
    "IN",
    "OUT"
]

# Accessory Details
accessories = [
    "Adapter",
    "Bolt Type",
    "Center",
    "Hub Nut",
    "Whole Nut",
    "Tire Valve",
]
nut_chocies = [
    "12 x 1.25 / 17mm",
    "12 x 1.5 / 17mm",
    "14 x 1.25 / 19mm",
    "14 x 1.25 / 21mm",
    "14 x 1.5 / 19mm",
    "14 x 1.5 / 21mm",
    "14 x 2.0 / 19mm",
    "14 x 2.0 / 21mm",
]
tire_valve = [
    'standard',
    'tire valve sensor',
]
adapter = [
    '4H/100',
    '4H/114.3',
    '5H/100',
    '5H/112',
    '5H/114.3',
    '5H/120',
    '6H/114.3',
    '6H/139.7',
]

# All transactions
def get_masterlist_data():
    cache_key = "masterlist_data"
    cached_data = cache.get(cache_key)

    if cached_data is not None:
        return cached_data
    
    masterlist = pd.DataFrame(get_all_rows())
    masterlist.fillna('', inplace=True)
    cache.set(cache_key, masterlist)

    masterlist = pd.DataFrame(get_all_rows())
    masterlist.fillna('', inplace=True)
    return masterlist

# All Tires
def get_tires_masterlist():
    cache_key = "tires_masterlist"
    cached_data = cache.get(cache_key)

    if cached_data is not None:
        return cached_data
    
    masterlist = get_masterlist_data()
    tires_masterlist = masterlist[masterlist['Type'] == 'Tires']
    cache.set(cache_key, tires_masterlist)
    return tires_masterlist

# All Magwheels
def get_magwheels_masterlist():
    cache_key = "magwheels_masterlist"
    cached_data = cache.get(cache_key)

    if cached_data is not None:
        return cached_data
    
    masterlist = get_masterlist_data()
    magwheels_masterlist = masterlist[masterlist['Type'] == 'Magwheels']
    cache.set(cache_key, magwheels_masterlist)
    return magwheels_masterlist

# Tires Brand Choices
def get_tires_brand_choices():
    cache_key = "tires_brand_choices"
    cached_data = cache.get(cache_key)

    if cached_data is not None:
        return cached_data
    
    tires_masterlist = get_tires_masterlist()
    tires_brand_choices = [(i, i) for i in sorted(tires_masterlist['Brand'].unique())]
    cache.set(cache_key, tires_brand_choices)
    return tires_brand_choices

# Tires Size Choices on Brand
def get_tires_brand_size_choices():
    cache_key = "tires_brand_size_choices"
    cached_data = cache.get(cache_key)

    if cached_data is not None:
        return cached_data
    
    tires_masterlist = get_tires_masterlist()
    size_grouped = tires_masterlist.groupby(['Brand', 'Size'])['Pattern / Model'].apply(lambda x: list(set(x))).to_dict()
    TIRES_BRAND_SIZE_CHOICES = {}

    for (brand, size), patterns in size_grouped.items():
        size = int(size)
        if brand not in TIRES_BRAND_SIZE_CHOICES:
            TIRES_BRAND_SIZE_CHOICES[brand] = {}
        TIRES_BRAND_SIZE_CHOICES[brand][size] = patterns
    cache.set(cache_key, TIRES_BRAND_SIZE_CHOICES)
    return TIRES_BRAND_SIZE_CHOICES

# Tires Model and Specs Choices
def get_tires_model_specs_choices():
    cache_key = "tires_model_specs_choices"
    cached_data = cache.get(cache_key)

    if cached_data is not None:
        return cached_data

    tires_masterlist = get_tires_masterlist()
    model_specs_choices = {}

    specs_grouped = tires_masterlist.groupby(['Pattern / Model', 'Size'])['Specs'].apply(lambda x: list(set(x))).to_dict()
    for (model, size), specs in specs_grouped.items():
        size = int(size)
        if model not in model_specs_choices:
            model_specs_choices[model] = {}
        model_specs_choices[model][size] = specs

    cache.set(cache_key, model_specs_choices)
    return model_specs_choices

# Tires Specs and Load Choices
def get_tires_specs_load_choices():
    cache_key = "tires_specs_load_choices"
    cached_data = cache.get(cache_key)

    if cached_data is not None:
        return cached_data

    tires_masterlist = get_tires_masterlist()
    specs_load_choices = (
        tires_masterlist.groupby('Specs')['Load / Speed Index']
        .apply(lambda x: list(set(x.fillna(''))))
        .to_dict()
    )

    cache.set(cache_key, specs_load_choices)
    return specs_load_choices

# Tires Specs and Remarks Choices
def get_tires_specs_remarks_choices():
    cache_key = "tires_specs_remarks_choices"
    cached_data = cache.get(cache_key)

    if cached_data is not None:
        return cached_data

    tires_masterlist = get_tires_masterlist()
    specs_remarks_choices = (
        tires_masterlist.groupby('Specs')['Remarks']
        .apply(lambda x: list(set(x.fillna(''))))
        .to_dict()
    )

    cache.set(cache_key, specs_remarks_choices)
    return specs_remarks_choices

# Magwheels Brand Choices
def get_magwheels_brand_choices():
    cache_key = "magwheels_brand_choices"
    cached_data = cache.get(cache_key)

    if cached_data is not None:
        return cached_data
    
    magwheels_masterlist = get_magwheels_masterlist()
    magwheel_brand_choices = [(i, i) for i in sorted(magwheels_masterlist['Brand'].unique())]
    cache.set(cache_key, magwheel_brand_choices)
    return magwheel_brand_choices

# Magwheels Brand and Size Choices
def get_magwheels_brand_size_choices():
    cache_key = "magwheels_brand_size_choices"
    cached_data = cache.get(cache_key)

    if cached_data is not None:
        return cached_data

    magwheels_masterlist = get_magwheels_masterlist()
    brand_size_choices = {}

    size_grouped = magwheels_masterlist.groupby(['Brand', 'Size'])['Pattern / Model'].apply(lambda x: list(set(x))).to_dict()
    for (brand, size), patterns in size_grouped.items():
        if brand not in brand_size_choices:
            brand_size_choices[brand] = {}
        brand_size_choices[brand][size] = patterns

    cache.set(cache_key, brand_size_choices)
    return brand_size_choices

# Magwheels Model and Color Choices
def get_magwheels_model_color_choices():
    cache_key = "magwheels_model_color_choices"
    cached_data = cache.get(cache_key)

    if cached_data is not None:
        return cached_data

    magwheels_masterlist = get_magwheels_masterlist()
    color_choices = {}

    color_grouped = magwheels_masterlist.groupby(['Pattern / Model', 'PCD 1'])['Color'].apply(lambda x: list(set(x))).to_dict()
    for (model, pcd1), color in color_grouped.items():
        if model not in color_choices:
            color_choices[model] = {}
        color_choices[model][pcd1] = color

    cache.set(cache_key, color_choices)
    return color_choices

# Magwheels Model and PCD 1 Choices
def get_magwheels_model_pcd1_choices():
    cache_key = "magwheels_model_pcd1_choices"
    cached_data = cache.get(cache_key)

    if cached_data is not None:
        return cached_data

    magwheels_masterlist = get_magwheels_masterlist()
    pcd1_choices = {}

    pcd1_grouped = magwheels_masterlist.groupby(['Pattern / Model', 'Size'])['PCD 1'].apply(lambda x: list(set(x))).to_dict()
    for (model, size), pcd1 in pcd1_grouped.items():
        if model not in pcd1_choices:
            pcd1_choices[model] = {}
        pcd1_choices[model][size] = pcd1

    cache.set(cache_key, pcd1_choices)
    return pcd1_choices

# Magwheels Model and PCD 2 Choices
def get_magwheels_model_pcd2_choices():
    cache_key = "magwheels_model_pcd2_choices"
    cached_data = cache.get(cache_key)

    if cached_data is not None:
        return cached_data

    magwheels_masterlist = get_magwheels_masterlist()
    pcd2_choices = {}

    pcd2_grouped = magwheels_masterlist.groupby(['Pattern / Model', 'PCD 1'])['PCD 2'].apply(lambda x: list(set(x))).to_dict()
    for (model, pcd1), pcd2 in pcd2_grouped.items():
        if model not in pcd2_choices:
            pcd2_choices[model] = {}
        pcd2_choices[model][pcd1] = pcd2

    cache.set(cache_key, pcd2_choices)
    return pcd2_choices

# Magwheels Model and Offset Choices
def get_magwheels_model_offset_choices():
    cache_key = "magwheels_model_offset_choices"
    cached_data = cache.get(cache_key)

    if cached_data is not None:
        return cached_data
    
    magwheels_masterlist = get_magwheels_masterlist()
    MAGWHEELS_MODEL_OFFSET_CHOICES = {}

    offset_grouped = magwheels_masterlist.groupby(['Pattern / Model', 'PCD 1'])['Offset'].apply(lambda x: list(set(x))).to_dict()
    for (model, pcd1), offset in offset_grouped.items():
        if model not in MAGWHEELS_MODEL_OFFSET_CHOICES:
            MAGWHEELS_MODEL_OFFSET_CHOICES[model] = {}
        MAGWHEELS_MODEL_OFFSET_CHOICES[model][pcd1] = offset
    
    cache.set(cache_key, MAGWHEELS_MODEL_OFFSET_CHOICES)
    return MAGWHEELS_MODEL_OFFSET_CHOICES

# Magwheels Model and Bore Choices
def get_magwheels_model_bore_choices():
    cache_key = "magwheels_model_bore_choices"
    cached_data = cache.get(cache_key)

    if cached_data is not None:
        return cached_data
    
    magwheels_masterlist = get_magwheels_masterlist()
    MAGWHEELS_MODEL_BORE_CHOICES = {}
    
    bore_grouped = magwheels_masterlist.groupby(['Pattern / Model', 'PCD 1'])['Hole Bore'].apply(lambda x: list(set(x))).to_dict()
    for (model, pcd1), bore in bore_grouped.items():
        if model not in MAGWHEELS_MODEL_BORE_CHOICES:
            MAGWHEELS_MODEL_BORE_CHOICES[model] = {}
        MAGWHEELS_MODEL_BORE_CHOICES[model][pcd1] = bore
    
    cache.set(cache_key, MAGWHEELS_MODEL_BORE_CHOICES)
    return MAGWHEELS_MODEL_BORE_CHOICES

# Magwheels Model and Color Choices
def get_magwheels_model_color_choices():
    cache_key = "magwheels_model_color_choices"
    cached_data = cache.get(cache_key)

    if cached_data is not None:
        return cached_data
    
    magwheels_masterlist = get_magwheels_masterlist()
    MAGWHEELS_MODEL_COLOR_CHOICES = {}
    
    color_grouped = magwheels_masterlist.groupby(['Pattern / Model', 'PCD 1'])['Color'].apply(lambda x: list(set(x))).to_dict()
    for (model, pcd1), color in color_grouped.items():
        if model not in MAGWHEELS_MODEL_COLOR_CHOICES:
            MAGWHEELS_MODEL_COLOR_CHOICES[model] = {}
        MAGWHEELS_MODEL_COLOR_CHOICES[model][pcd1] = color

    cache.set(cache_key, MAGWHEELS_MODEL_COLOR_CHOICES)    
    return MAGWHEELS_MODEL_COLOR_CHOICES

### Dependent Global Variables
center_cap = sorted(
    [brand for brand in [type for type in [get_tires_brand_choices(), get_magwheels_brand_choices()]]]
)