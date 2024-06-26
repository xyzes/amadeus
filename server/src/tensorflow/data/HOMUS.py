from omrdatasettools import Downloader, OmrDataset

downloader = Downloader()
downloader.download_and_extract_dataset(OmrDataset.Homus_V2, "raw")

from omrdatasettools import HomusImageGenerator

HomusImageGenerator.create_images(raw_data_directory="raw",
                                  destination_directory="labeled",
                                  stroke_thicknesses=[3],
                                  canvas_width=96,
                                  canvas_height=192,
                                  staff_line_spacing=14,
                                  staff_line_vertical_offsets=None)