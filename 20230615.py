import dearpygui.dearpygui as dpg
import dearpygui.demo as demo


# Библиотека для красивого графического интерфейса
# https://youtu.be/Fkpr0au59aU
# https://github.com/Zproger/code_lessons/tree/main/videos/%D0%BA%D1%80%D0%B0%D1%81%D0%B8%D0%B2%D1%8B%D0%B9_%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D1%84%D0%B5%D0%B9%D1%81_%D0%BD%D0%B0_python



dpg.create_context()
dpg.create_viewport(title='Custom Title', width=800, height=600)

demo.show_demo()

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
