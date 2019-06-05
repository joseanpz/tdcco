from pydantic import BaseModel
import pickle
import numpy as np
from xgboost import DMatrix


xgb_model = pickle.load(open('app/solicitud/bmodels/xgb.model', 'rb'))


class Solicitud(BaseModel):
    ds_cl: float = None
    ds_ol_cl: float = None
    dpcv_cap: float = None
    ms_op: float = None
    dias_atraso: float = None
    utilizacion: float = None
    months_on_file_banking: float = None
    pi: float = None
    min_vp_mes_t00: float = None
    avg2_vp_mes_t00: float = None

    def predecir(self):
        solicitud_arreglo = np.array(list(self)).T
        columnas = solicitud_arreglo[0]
        valores = solicitud_arreglo[1].reshape(1, -1)
        valores = xgb_model.scaler.transform(xgb_model.imputer.transform(valores))
        dmatriz = DMatrix(data=valores, feature_names=columnas)
        return float(xgb_model.booster.predict(dmatriz)[0])

