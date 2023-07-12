from infre.models import SetBased, GSB, GSBWindow, PGSB, PGSBW, ConGSB, ConGSBWindow
from numpy import mean
from networkx import to_numpy_array
from infre.preprocess import Collection


if __name__ == '__main__':

    path = 'collections/CF/docs'


    # create collection
    col = Collection(path).create(first=-1)
    
    # load queries, relevant documents
    queries, rels = Collection.load_qd('collections/CF', prep=False)


    ########## CONCEPTUALIZED GRAPHICAL SET BASED ####################  .226 (raw queries)
    con_gsb_model = ConGSB(col, clusters=110, cond={'sim': 0.5}).fit(queries)
    pre, rec = con_gsb_model.evaluate(rels)

    print(f'CGSB: {mean(pre):.3f}, {mean(rec):.3f}')
    print(con_gsb_model.graph.number_of_nodes(), con_gsb_model.graph.number_of_edges())
    
  
    ######### CONCEPTUALIZED GRAPHICAL SET BASED Window ####################  
    # con_gsbw_model = ConGSBWindow(col, window=.15, clusters=50, cond={'sim':.2}).fit(queries)
    # pre, rec = con_gsbw_model.evaluate(rels)

    # print(f'CGSBW: {mean(pre):.3f}, {mean(rec):.3f}')
    # print(con_gsbw_model.graph.number_of_nodes(), con_gsbw_model.graph.number_of_edges())