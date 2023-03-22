import pandas as pd
from loguru import logger
from def_app import insert_devoluciones

if __name__ == "__main__":
    
    
        
        df_lista_devol = pd.read_excel("a-x.xlsx")
        
        #modificar el formato de la fecha
        df_lista_devol["Fecha de Trx"] = df_lista_devol["Fecha de Trx"].dt.strftime("%Y-%m-%dT%H:%M:%S-05:00")
        
        # Reemplazar los valores de la columna "Moneda"
        df_lista_devol["Moneda"] = df_lista_devol["Moneda"].replace({"Soles": "SOL"})
        
        # Reemplazar los valores de la columna Tipo de devolucion"
        df_lista_devol["Tipo de devolucion"] = df_lista_devol["Tipo de devolucion"].replace({"COMPLETA": 1, "PARCIAL": 2})
        
        ss = list(
            zip(
                df_lista_devol["Nº Pedido"],
                df_lista_devol["Cod Comercio ALG"],
                df_lista_devol["Importe Devolucion"],
                df_lista_devol["Tipo de devolucion"],
                df_lista_devol["Moneda"],
                df_lista_devol["PAN"],
                df_lista_devol["Importe del Pedido"],
                df_lista_devol["Cod. Autorizacion"],
                df_lista_devol["Fecha de Trx"],
            )
        )
    
        devolicion = insert_devoluciones(ss)
        print(devolicion)

