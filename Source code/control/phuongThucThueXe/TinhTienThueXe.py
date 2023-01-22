from abc import ABC, abstractmethod

class TinhTienThueXe(ABC):
    @abstractmethod
    def tinhTien(self,thoiDiemDau,thoiDiemCuoi,k=1):
        pass