VEHICLE_BRAND = (
    ('HD', 'HONDA'),
    ('HY', 'HYUNDAI'),
    ('MS', 'MARUTI SUZUKI'),
    ('TT', 'TATA'),
    ('MH', 'MAHINDRA'),
    ('TY', 'TOYOTA'),
)

VEHICLE_MODEL = {
    'HD': ['CY', 'AM', 'BR', 'JZ', 'CV'],
    'HY': ['XC', 'IT', 'CR', 'EL'],
    'MS': ['CZ', 'WR', 'DZ', 'ZS', 'AT'],
    'TT': ['IN', 'ZT', 'HX'],
    'MH': ['BO', 'SP', 'XL', 'TU', 'KV', 'TL'],
    'TY': ['ET', 'FT', 'IC', 'BL']
}

VEHICLE_MODEL_OBJ = {
    'CY': 'CITY', 'AM': 'AMAZE', 'BR': 'BRIO', 'JZ': 'JAZZ',
    'CV': 'CIVIC', 'XC': 'XCENT', 'IT': 'I20 ACTIVE', 'CR': 'CRETA',
    'EL': 'ELANTRA','CZ': 'CIAZ', 'WR': 'WAGON R', 'DZ': 'DEZIRE',
    'ZS': 'ZEN SUV', 'AT': 'ALTO K10', 'IN': 'INDICA CR4',
    'ZT': 'ZEST', 'HX': 'HEXA', 'BO': 'BOLERO', 'SP': 'SCORPIO',
    'XL': 'XYLO', 'TU': 'TUV300', 'KV': 'KUV 100 NXT', 'TL': 'TUV 300 L',
    'ET': 'ETIOS LIVA', 'FT': 'FORTUNER', 'IC': 'INOVA CRYSTA', 'BL': 'BALINO'
}

def vehicle_brand():
    return VEHICLE_BRAND

def get_vehicle_brand():
    response = {data[0]: data[1] for data in VEHICLE_BRAND}
    return response