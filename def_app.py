# funcion para insertar los datos en la tabla sqmbox.tbox_devoluciones


def insert_devoluciones(ss):
        # Recorrer la lista de resultados e insertar los valores
        lista = []
        for value in ss:
            consulta = f"INSERT INTO sqmbox.tbox_devoluciones(vc_numeropedido,vc_idcomercio,nu_monto_devo,in_tipo,ch_currency,vc_cardnumber,nu_monto_trx,vc_codigoautorizacion,dt_fecha_trx) VALUES ('{value[0]}', '{value[1]}', {value[2]}, {value[3]}, '{value[4]}', '{value[5]}', {value[6]}, '{value[7]}', '{value[8]}')"
            lista.append(consulta)
            
        return lista
