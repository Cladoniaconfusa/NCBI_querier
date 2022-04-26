import ssl
from Bio import Entrez
from NCBI_querier_printer import Fetching_data

ssl._create_default_https_context = ssl._create_unverified_context

def Obtener_registros(id_list)-> dict:
    data ={'locus':[],'length':[],'strandedness':[],'Topology':[],'division':[],'Primary accesion':[],'Organism':[]}
    for i in id_list:
        Fetching_data(i)
        busqueda_id = Entrez.efetch(db='nucleotide', id = i, rettype='gb', retmode = 'xml')
        doomie = next(Entrez.parse(busqueda_id))
        data['locus'].append(doomie['GBSeq_locus'])
        data ['length'].append(doomie['GBSeq_length'])
        data['strandedness'].append(doomie['GBSeq_strandedness'])
#        data['moltype'].append(doomie['GBSeq_moltype'])
        data['Topology'].append(doomie['GBSeq_topology'])
        data['division'].append(doomie['GBSeq_division']) 
        data['Primary accesion'].append(doomie['GBSeq_primary-accession'])
        data['Organism'].append(doomie['GBSeq_organism'])
#        data['Taxonomy'].append(doomie['GBSeq_taxonomy'])
    #con fetch se recogen los datos de cada id, luego se separan en un diccionario
    return data