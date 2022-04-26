from Bio import Entrez
from NCBI_querier_searchids import Obtener_registros
from NCBI_querier_exportXML import exportar_pandas
from NCBI_querier_printer import Encabezado,Generando_IDs,Lista_IDs_generada
import sys
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def start()->tuple: 
    #query,email,max_recrds y file_name del csv resultante
    Encabezado()
    query = sys.argv[1]
    Entrez.email = sys.argv[2]
    max_records = sys.argv[3]
    file_name = sys.argv[4]
    return query,max_records, file_name

def busqueda_ncbi_ids(query,max_records)->list:
    Generando_IDs()
    doomie_search = Entrez.esearch(db='Nucleotide', retmax = max_records, term = query)
    reg = Entrez.read(doomie_search)
    id_list = reg['IdList']
    Lista_IDs_generada(id_list)
    return(id_list)

def main()-> None:
    query, max_records, file_name = start()
    id_list = busqueda_ncbi_ids(query, max_records)
    data = Obtener_registros(id_list)
    exportar_pandas(data,file_name)

if __name__ == "__main__":
    main()

