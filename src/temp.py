import tkinter
import tkintermapview

# create tkinter window
root_tk = tkinter.Tk()
root_tk.geometry(f"{1000}x{700}")
root_tk.title("map_view_simple_example.py")

# create map widget
map_widget = tkintermapview.TkinterMapView(root_tk, width=1000, height=700, corner_radius=0)
map_widget.pack(fill="both", expand=True)

# set other tile server (standard is OpenStreetMap)
# map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)  # google normal
# map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)  # google satellite

# set current position and zoom
map_widget.set_position(28.214790, -82.622370, marker=False)  # Berlin, Germany
map_widget.set_zoom(7)




# set a position marker (also with a custom color and command on click)
marker_2 = map_widget.set_marker(28.214790, -82.622370, text="")
marker_3 = map_widget.set_marker(29.643946, -82.355659, text="")
# marker_3.set_position(...)
# marker_3.set_text(...)
# marker_3.delete()

# set a path
path_1 = map_widget.set_path([marker_2.position, marker_3.position])
# path_1.add_position(...)
# path_1.remove_position(...)
# path_1.delete()

root_tk.mainloop()