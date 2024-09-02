from database import Database
from product_analyzer import ProductAnalyzer  


if __name__ == "__main__":

  db = Database(database="mercado", collection="compras")

  product_analyzer = ProductAnalyzer(database="mercado", collection="compras")

product_analyzer.total_vendas_diario()  
product_analyzer.produto_mais_vendido()  
product_analyzer.cliente_que_mais_gastou()  
product_analyzer.produtos_vendidos_acima_de_um()

