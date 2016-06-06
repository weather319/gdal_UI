# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHeaderView
import sys


''''''

class Gis_DrawTree(object):
	"""输入一个pandas的frame，执行一个构造列表的行为"""

	def get_maplist(self,frame):
		self.maplist = frame

	def get_timelist(self):
		"""把所有的时间，分片为年排列"""
		self.time_year = []
		self.time_month = []
		for i in range(len(self.maplist.index)):
			self.time_year.append(self.maplist.Time[i].split('-')[0])
			self.time_month.append(self.maplist.Time[i].split('-')[1])

	def build_maplist_from_year(self):
		self.get_timelist()
		map_dict = {}

		for year in self.time_year:
			map_dict[year] = \
				self.maplist[(self.maplist.Time >= year) & \
						(self.maplist.Time < str(int(year)+1))].MapId.tolist()
		print (map_dict)
		self.map_dict = map_dict

	def get_Qtree(self,Qtree):
		self.Qtree = Qtree
		self.Qtree.setColumnCount(2)
		self.Qtree.setHeaderLabels(['时间','地图列表'])

	def draw_tree(self,frame,tree):
		self.get_Qtree(tree)
		self.get_maplist(frame)
		self.build_maplist_from_year()
		#self.map_dict = frame
		i = 0
		for year in self.map_dict:
			item_0 = QtWidgets.QTreeWidgetItem(self.Qtree)
			self.Qtree.topLevelItem(i).setText(0, year)
			j = 0
			for mapid in self.map_dict[year]:
				item_1 = QtWidgets.QTreeWidgetItem(item_0)
				self.Qtree.topLevelItem(i).child(j).setText(0, self.time_month[j]+'月')
				self.Qtree.topLevelItem(i).child(j).setText(1, mapid)
				j = j+1
			i = i+1
		return self.Qtree

def main():
	map_dict = {'1991':[u'LT51190381991204BJC00'],\
				'1992':[u'LT51190381991204BJC02']}
	print (map_dict)
	app = QtWidgets.QApplication(sys.argv)
	tree = QtWidgets.QTreeWidget()
	DT = Gis_DrawTree()
	tree = DT.draw_tree(map_dict,tree)
	tree.show()
	sys.exit(app.exec_())


if __name__ == "__main__":
	main()








