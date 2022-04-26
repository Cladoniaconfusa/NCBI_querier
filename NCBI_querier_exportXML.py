import pandas as pd
from NCBI_querier_printer import Preparing_tsvfile, Completado

def exportar_pandas(data,file_name)-> None:
    Preparing_tsvfile(file_name)
    doomie_pd = pd.DataFrame(data)
    doomie_pd.to_csv(file_name, sep='\t')
    Completado()