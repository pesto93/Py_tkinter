"""
_author_ = Johnleonard C.O
_Created_ =  12/5/2019
"""
from tkinter import *
import tkinter.messagebox
from src.backend import *
from pandastable import Table


class FirstAmerica:

	@staticmethod
	def exit():
		i_exit = tkinter.messagebox.askyesno("First American Database Management Systems", "Confirm if you want to exit")
		if i_exit > 0:
			root.destroy()
		return

	def clear_data(self):
		self.entry_streetname.delete(0, END)
		self.entry_city.delete(0, END)
		self.entry_net_floor_area.delete(0, END)
		self.entry_nr_units.delete(0, END)
		self.entry_sqft_price.delete(0, END)
		self.entry_construction_year.delete(0, END)
		self.entry_buildingarea.delete(0, END)

	def __init__(self, root):
		self.root = root
		self.root.title("Database Management Systems")
		self.root.geometry("1350x750+0+0")
		self.root.config(bg="cadet blue")

		self.street_name = StringVar()
		self.city = StringVar()
		self.net_floor_area = StringVar()
		self.nr_units = StringVar()
		self.sqft_price = StringVar()
		self.construction_year = StringVar()
		self.buildingarea = StringVar()

		# -------------------------- frames --------------------------

		main_frame = Frame(self.root, bg="cadet blue")
		main_frame.grid()

		tittle_frame = Frame(main_frame, bd=2, padx=54, pady=8, bg="Ghost white", relief=RIDGE)
		tittle_frame.pack(side=TOP)
		self.lbl_title = Label(tittle_frame, font=('arial', 37, 'bold'), text="First American Database Management Systems", bg="Ghost white")
		self.lbl_title.grid()

		button_frame = Frame(main_frame, bd=2, width=1350, height=70, padx=18, pady=10, bg="Ghost white", relief=RIDGE)
		button_frame.pack(side=BOTTOM)

		info_frame = Frame(main_frame, bd=1, width=1300, height=400, padx=20, pady=20, bg="cadet blue", relief=RIDGE)
		info_frame.pack(side=BOTTOM)

		info_frame_left = LabelFrame(info_frame, bd=1, width=1000, height=600, padx=20, pady=20, bg="Ghost white", relief=RIDGE,
		                             font=('arial', 20, 'bold'), text="Property info\n")
		info_frame_left.pack(side=LEFT)

		# -------------------------- labels and Entry widget --------------------------

		self.lbl_streetname = Label(info_frame_left, font=('arial', 20, 'bold'), text="Street Name :", padx=2, pady=2, bg="Ghost white")
		self.lbl_streetname.grid(row=0, column=0, sticky=W)
		self.entry_streetname = Entry(info_frame_left, font=('arial', 20, 'bold'), textvariable=self.street_name, width=39)
		self.entry_streetname.grid(row=0, column=1)

		self.lbl_city = Label(info_frame_left, font=('arial', 20, 'bold'), text="City :", padx=2, pady=2, bg="Ghost white")
		self.lbl_city.grid(row=1, column=0, sticky=W)
		self.entry_city = Entry(info_frame_left, font=('arial', 20, 'bold'), textvariable=self.city, width=39)
		self.entry_city.grid(row=1, column=1)

		self.lbl_net_floor_area = Label(info_frame_left, font=('arial', 20, 'bold'), text="Total Living Area :", padx=2, pady=2, bg="Ghost white")
		self.lbl_net_floor_area.grid(row=2, column=0, sticky=W)
		self.entry_net_floor_area = Entry(info_frame_left, font=('arial', 20, 'bold'), textvariable=self.net_floor_area, width=39)
		self.entry_net_floor_area.grid(row=2, column=1)

		self.lbl_nr_units = Label(info_frame_left, font=('arial', 20, 'bold'), text="Nr units :", padx=2, pady=2, bg="Ghost white")
		self.lbl_nr_units.grid(row=3, column=0, sticky=W)
		self.entry_nr_units = Entry(info_frame_left, font=('arial', 20, 'bold'), textvariable=self.nr_units, width=39)
		self.entry_nr_units.grid(row=3, column=1)

		self.lbl_sqft_price = Label(info_frame_left, font=('arial', 20, 'bold'), text="Sqft Price :", padx=2, pady=2, bg="Ghost white")
		self.lbl_sqft_price.grid(row=4, column=0, sticky=W)
		self.entry_sqft_price = Entry(info_frame_left, font=('arial', 20, 'bold'), textvariable=self.sqft_price, width=39)
		self.entry_sqft_price.grid(row=4, column=1)

		self.lbl_construction_year = Label(info_frame_left, font=('arial', 20, 'bold'), text="Year Built :", padx=2, pady=2, bg="Ghost white")
		self.lbl_construction_year.grid(row=5, column=0, sticky=W)
		self.entry_construction_year = Entry(info_frame_left, font=('arial', 20, 'bold'), textvariable=self.construction_year, width=39)
		self.entry_construction_year.grid(row=5, column=1)

		self.lbl_buildingarea = Label(info_frame_left, font=('arial', 20, 'bold'), text="Building Area :", padx=2, pady=2, bg="Ghost white")
		self.lbl_buildingarea.grid(row=6, column=0, sticky=W)
		self.entry_buildingarea = Entry(info_frame_left, font=('arial', 20, 'bold'), textvariable=self.buildingarea, width=39)
		self.entry_buildingarea.grid(row=6, column=1)

		# -------------------------- Button widget --------------------------

		self.btn_search = Button(button_frame, text='Search', font=('arial', 20, 'bold'), height=1, width=10, bd=4, command=self.dialog)
		self.btn_search.grid(row=0, column=0)

		self.btn_clear = Button(button_frame, text='Clear', font=('arial', 20, 'bold'), height=1, width=10, bd=4, command=self.clear_data)
		self.btn_clear.grid(row=0, column=1)

		self.btn_exit = Button(button_frame, text='Exit', font=('arial', 20, 'bold'), height=1, width=10, bd=4, command=self.exit)
		self.btn_exit.grid(row=0, column=2)

	def dialog(self):
		data = self.search()
		d = LoadTable(root, data)
		root.wait_window(d.top)

	def search(self):
		res = None
		street_name = self.street_name.get()
		city = self.city.get()
		net_floor_area = self.net_floor_area.get()
		nr_units = self.nr_units.get()
		sqft_price = self.sqft_price.get()
		construction_year = self.construction_year.get()
		buildingarea = self.buildingarea.get()

		if len(street_name) and len(city) and len(net_floor_area) and len(nr_units) and len(sqft_price) and len(construction_year) and len(
				buildingarea) != 0:
			print('1st condition')
			res = open_connection(street_name, city, net_floor_area, nr_units, sqft_price, construction_year, buildingarea, 1)
			return res

		elif len(city) and len(net_floor_area) and len(nr_units) and len(sqft_price) and len(construction_year) and len(buildingarea) != 0:
			print('2nd condition')
			res = open_connection(street_name, city, net_floor_area, nr_units, sqft_price, construction_year, buildingarea, 2)
			return res

		elif len(city) and len(sqft_price) and len(nr_units) and len(construction_year) and len(street_name) and len(buildingarea) != 0:
			print('3rd condition')
			res = open_connection(street_name, city, net_floor_area, nr_units, sqft_price, construction_year, buildingarea, 3)
			return res

		elif len(city) and len(sqft_price) and len(nr_units) and len(buildingarea) and len(construction_year) != 0:
			print('4th condition')
			res = open_connection(street_name, city, net_floor_area, nr_units, sqft_price, construction_year, buildingarea, 4)
			return res
		else:
			return res


class LoadTable:
	def __init__(self, parent, df):
		self.top = Toplevel(parent)
		self.top.title("Table Result")
		self.top.geometry("1000x750+0+0")
		self.top.config(bg="cadet blue")

		f = Frame(self.top)
		f.pack(fill=BOTH, expand=1)
		print(df)
		self.table = pt = Table(f, dataframe=df, showtoolbar=True, showstatusbar=True)
		pt.show()


if __name__ == '__main__':
	root = Tk()
	application = FirstAmerica(root)
	root.mainloop()
