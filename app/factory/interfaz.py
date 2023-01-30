from abc import abstractmethod

class AbstractReport:
    
    @abstractmethod
    def get_sales_by_each_product(self):
        pass
   