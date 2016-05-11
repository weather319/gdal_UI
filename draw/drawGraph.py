#!/usr/bin/env python
# -*- coding: utf-8 -*- 

  
import cairo   
import pycha.pie  
import pycha.bar  
import pycha.scatter  
import pycha.stackedbar  
import pycha.line 

  
#设置画布  
def set_charvalue():  
    width,height=200,150   
    surface=cairo.ImageSurface(cairo.FORMAT_ARGB32,width,height)   
    return surface  
      
#画饼图  
def draw_pie(surface, options, dataSet):  
    chart=pycha.pie.PieChart(surface,options)   
    chart.addDataset(dataSet)   
    chart.render()   
    surface.write_to_png('./Pie.png')   
  
#垂直直方图  
def draw_vertical_bar(surface, options, dataSet):  
    chart=pycha.bar.VerticalBarChart(surface,options)   
    chart.addDataset(dataSet)   
    chart.render()   
    surface.write_to_png('./vertical_bar.png')     
   
#垂直水平直方图      
def draw_horizontal_bar(surface, options, dataSet):  
    chart = pycha.bar.HorizontalBarChart(surface,options)   
    chart.addDataset(dataSet)   
    chart.render()   
    surface.write_to_png('./horizontal_bar.png')     
      
#线图      
def draw_line(surface, options, dataSet):  
    chart = pycha.line.LineChart(surface,options)   
    chart.addDataset(dataSet)   
    chart.render()   
    surface.write_to_png('./line.png')        
  
#点图      
def draw_scatterplot(surface, options, dataSet):  
    chart = pycha.scatter.ScatterplotChart(surface,options)   
    chart.addDataset(dataSet)   
    chart.render()   
    surface.write_to_png('./scatterplotChart.png')           
  
#垂直块图       
def draw_stackedverticalbarChar(surface, options, dataSet):  
    chart = pycha.stackedbar.StackedVerticalBarChart(surface,options)   
    chart.addDataset(dataSet)   
    chart.render()   
    surface.write_to_png('./stackedVerticalBarChart.png')        
  
#水平块图  
def draw_stackedhorizontalbarChart(surface, options, dataSet):  
    chart = pycha.stackedbar.StackedHorizontalBarChart(surface,options)   
    chart.addDataset(dataSet)   
    chart.render()   
    surface.write_to_png('./stackedhorizontalbarChart.png')      
      
if __name__ == '__main__':  
    ''''' 
    Function:使用pycha画各种图表 
    Input：NONE 
    Output: NONE 
    author: socrates 
    blog:http://blog.csdn.net/dyx1024 
    date:2012-02-28 
    '''  
    #数据来源  
    dataSet=(   
             ('Total Nitrogen',((0,1),(0.2,2),(0.4,3))),   
             ('Chlorophyll',((1,2),(1.2,4),(1.4,3))),   
             ('Dissolved Oxygen',((2,5),(2.2,1,),(2.4,0.5))),   
             ('CODMn',((3,3),(3.2,2,),(3.4,1.5))),   
            )   
    
    #图像属性定义  
    options={   
                'legend':{'hide':False},   
                'title': '叶绿素-线图（太湖）',  
                'titleColor':'#0000ff',  
                'titleFont':'字体',  
                'background':{'chartColor': '#ffffff'},   
                'axis':{'labelColor':'#ff0000'},  
            }       
      
      
    surface = set_charvalue()  
      
    #根据需要调用不同函数画不同形状的图  
    #draw_pie(surface, options, dataSet)  
    draw_vertical_bar(surface, options, dataSet)  
    #draw_horizontal_bar(surface, options, dataSet)  
    #draw_scatterplot(surface, options, dataSet)  
    #draw_stackedverticalbarChar(surface, options, dataSet)  
    #draw_stackedhorizontalbarChart(surface, options, dataSet)  
    draw_line(surface, options, dataSet)  
      
          
