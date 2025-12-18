from kmk.extensions.encoder import Encoder
from kmk.keys import KC
from pins import ENC_A, ENC_B

encoder_handler = Encoder(
    pins=((ENC_A, ENC_B),),
    map=(
        ((KC.VOLD, KC.VOLU),),   # BASE
        ((KC.LEFT, KC.RIGHT),), # FN
        ((KC.MPRV, KC.MNXT),),  # MEDIA
    )
)