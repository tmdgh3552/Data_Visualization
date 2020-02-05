from datetime import time

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QDragEnterEvent, QDropEvent


def dragEnterEvent(self, e: QDragEnterEvent):
    if e.mimeData().hasText():
        text = e.mimeData().text()
        text_type = text[:8]
        self.path = text[8:]
        if text_type == "file:///" and os.path.isfile(self.path):
            e.accept()
    else:
        e.ignore()


def dropEvent(self, e: QDropEvent):
    if self.video is not None:
        self.push_stop()
        while self.video.cap.isOpened() is True:
            time.sleep(0.1)
        self.video.cap.release()
        self.video_slider.video_flag = False
        # TO DO
        # add release shot list info and it's file close

    self.video = Video(self.path)
    self.video_slider.video_flag = True
    # TO DO
    # add shot list file open and loading it

    if self.video.open_video():
        self.setWindowTitle("Shot Change Labeling Tool: " + os.path.basename(self.path))
        self.video_info_total_frames.setText("Total Frames: " + str(self.video.frame_count))

        self.image_label.setFixedSize(QSize(640, 480))
        height = 480 if self.video.frame_height <= 480 else self.video.frame_height
        self.resize(self.sizeHint())
        self.video_clip_group.setFixedSize(QSize(640 + self.image_width_margin,
                                                 height + self.image_height_margin))
        self.image_label.setFixedSize(QSize(self.video.frame_width,
                                            self.video.frame_height))

        self.update_image()
        self.video_slider.setMaximum(self.video.frame_count - 1)

        # set enabled all contents
        self.push_button_play.setDisabled(False)
        self.video_slider.setDisabled(False)

        # set button enable by it's condition
        self.shot_control_group.setEnabled(True)
        # self.push_button_shot_next.setEnabled(True)
        # self.push_button_shot_prev.setEnabled(True)
        # self.push_button_shot_insert.setEnabled(True)
        # self.push_button_shot_delete.setEnabled(True)
        # self.push_button_shot_load.setEnabled(True)
        # self.push_button_shot_save.setEnabled(True)

        if self.exists_shot_list_file() == True:
            self.push_load_shot()
        else:
            self.shot_list = [0]

        self.load_temporal_video_data()
        self.update_temporal_video_shot_vline()