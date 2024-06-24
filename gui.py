import sys
import os
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, 
                             QFileDialog, QSpinBox, QComboBox, QMessageBox)
from PyQt5.QtCore import Qt

# Import the encoding and decoding functions
from lazyown_infinitestorage import encode_file_to_video, decode_video_to_file

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("LazyOwn Infinite Storage")
        self.layout = QVBoxLayout()

        self.mode_combobox = QComboBox()
        self.mode_combobox.addItems(["encode", "decode"])
        self.mode_combobox.currentIndexChanged.connect(self.change_mode)

        self.layout.addWidget(QLabel("Mode:"))
        self.layout.addWidget(self.mode_combobox)

        self.encode_ui = None
        self.decode_ui = None

        self.create_common_ui()
        self.change_mode()

        self.setLayout(self.layout)

    def create_encode_ui(self):
        encode_ui = QVBoxLayout()

        self.input_file_label = QLabel("Select ZIP file:")
        self.input_file_edit = QLineEdit()
        self.input_file_button = QPushButton("Browse")
        self.input_file_button.clicked.connect(self.browse_input_file)

        self.output_file_label = QLabel("Video name:")
        self.output_file_edit = QLineEdit()

        file_layout = QHBoxLayout()
        file_layout.addWidget(self.input_file_edit)
        file_layout.addWidget(self.input_file_button)
        
        encode_ui.addWidget(self.input_file_label)
        encode_ui.addLayout(file_layout)
        encode_ui.addWidget(self.output_file_label)
        encode_ui.addWidget(self.output_file_edit)

        self.fps_label = QLabel("Frames per second:")
        self.fps_spinbox = QSpinBox()
        self.fps_spinbox.setRange(1, 60)
        self.fps_spinbox.setValue(30)
        
        encode_ui.addWidget(self.fps_label)
        encode_ui.addWidget(self.fps_spinbox)

        return encode_ui

    def create_decode_ui(self):
        decode_ui = QVBoxLayout()

        self.input_file_label = QLabel("Select Video file:")
        self.input_file_edit = QLineEdit()
        self.input_file_button = QPushButton("Browse")
        self.input_file_button.clicked.connect(self.browse_input_file)

        self.output_file_label = QLabel("Recovery ZIP file name:")
        self.output_file_edit = QLineEdit()

        file_layout = QHBoxLayout()
        file_layout.addWidget(self.input_file_edit)
        file_layout.addWidget(self.input_file_button)
        
        decode_ui.addWidget(self.input_file_label)
        decode_ui.addLayout(file_layout)
        decode_ui.addWidget(self.output_file_label)
        decode_ui.addWidget(self.output_file_edit)

        return decode_ui

    def create_common_ui(self):
        self.frame_size_label = QLabel("Frame size (width height):")
        self.width_spinbox = QSpinBox()
        self.width_spinbox.setRange(1, 10000)
        self.width_spinbox.setValue(640)
        self.height_spinbox = QSpinBox()
        self.height_spinbox.setRange(1, 10000)
        self.height_spinbox.setValue(480)
        frame_size_layout = QHBoxLayout()
        frame_size_layout.addWidget(self.width_spinbox)
        frame_size_layout.addWidget(self.height_spinbox)
        self.layout.addWidget(self.frame_size_label)
        self.layout.addLayout(frame_size_layout)

        self.block_size_label = QLabel("Block size:")
        self.block_size_spinbox = QSpinBox()
        self.block_size_spinbox.setRange(1, 100)
        self.block_size_spinbox.setValue(4)
        self.layout.addWidget(self.block_size_label)
        self.layout.addWidget(self.block_size_spinbox)

        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_process)
        self.layout.addWidget(self.start_button)

    def change_mode(self):
        mode = self.mode_combobox.currentText()

        if self.encode_ui:
            self.clear_layout(self.encode_ui)
            self.layout.removeItem(self.encode_ui)
        if self.decode_ui:
            self.clear_layout(self.decode_ui)
            self.layout.removeItem(self.decode_ui)

        if mode == "encode":
            self.encode_ui = self.create_encode_ui()
            self.layout.insertLayout(2, self.encode_ui)
            self.fps_label.show()
            self.fps_spinbox.show()
        else:
            self.decode_ui = self.create_decode_ui()
            self.layout.insertLayout(2, self.decode_ui)
            self.fps_label.hide()
            self.fps_spinbox.hide()

    def clear_layout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def browse_input_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        if self.mode_combobox.currentText() == "encode":
            file, _ = QFileDialog.getOpenFileName(self, "Select ZIP file", "", "ZIP Files (*.zip);;All Files (*)", options=options)
        else:
            file, _ = QFileDialog.getOpenFileName(self, "Select Video file", "", "Video Files (*.mp4);;All Files (*)", options=options)
        if file:
            self.input_file_edit.setText(file)

    def start_process(self):
        input_file = self.input_file_edit.text()
        output_file = self.output_file_edit.text()
        frame_size = (self.width_spinbox.value(), self.height_spinbox.value())
        block_size = self.block_size_spinbox.value()
        mode = self.mode_combobox.currentText()

        try:
            if mode == "encode":
                fps = self.fps_spinbox.value()
                output_file_with_resolution = f"{os.path.splitext(output_file)[0]}_{frame_size[0]}x{frame_size[1]}.mp4"
                encode_file_to_video(input_file, output_file_with_resolution, frame_size, fps, block_size)
            elif mode == "decode":
                decode_video_to_file(input_file, output_file, block_size)

            self.show_message("Process completed successfully!")
        except Exception as e:
            self.show_message(f"An error occurred: {str(e)}")

    def show_message(self, message):
        message_box = QMessageBox()
        message_box.setText(message)
        message_box.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
