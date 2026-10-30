# pip install cinereader https://pypi.org/project/cinereader/
# pip install tifffile https://pypi.org/project/tifffile/
import numpy as np
import cinereader as cr
import csv
from tifffile import TiffFile, imread, imwrite

def cine_metadata_to_dict_metadata(cine_metadata):
    """
    Convert CINE metadata to TIFF metadata dictionary for use with tifffile.imwrite().
    
    Args:
        cine_metadata: Instance of MetaData class containing CINE file information
        
    Returns:
        dict: TIFF metadata dictionary with keys like 'axes', 'resolution', etc.
    """
    tiff_metadata = {}
    
    # ===== CINE FILE HEADER =====
    if cine_metadata.Type is not None:
        tiff_metadata['cine_type'] = str(cine_metadata.Type)
    
    if cine_metadata.HeaderSize is not None:
        tiff_metadata['cine_header_size'] = int(cine_metadata.HeaderSize)
    
    if cine_metadata.Compression is not None:
        tiff_metadata['cine_compression'] = str(cine_metadata.Compression)
    
    if cine_metadata.Version is not None:
        tiff_metadata['cine_version'] = str(cine_metadata.Version)
    
    if cine_metadata.FirstMovieImage is not None:
        tiff_metadata['first_movie_image'] = int(cine_metadata.FirstMovieImage)
    
    if cine_metadata.TotalImageCount is not None:
        tiff_metadata['total_image_count'] = int(cine_metadata.TotalImageCount)
    
    if cine_metadata.FirstImageNo is not None:
        tiff_metadata['first_image_no'] = int(cine_metadata.FirstImageNo)
    
    if cine_metadata.ImageCount is not None:
        tiff_metadata['image_count'] = int(cine_metadata.ImageCount)
    
    if cine_metadata.OffImageHeader is not None:
        tiff_metadata['offset_image_header'] = int(cine_metadata.OffImageHeader)
    
    if cine_metadata.OffSetup is not None:
        tiff_metadata['offset_setup'] = int(cine_metadata.OffSetup)
    
    if cine_metadata.OffImageOffsets is not None:
        tiff_metadata['offset_image_offsets'] = int(cine_metadata.OffImageOffsets)
    
    if cine_metadata.TriggerTime is not None:
        tiff_metadata['trigger_time'] = str(cine_metadata.TriggerTime)
    
    if cine_metadata.TriggerTime_displ is not None:
        tiff_metadata['trigger_time_display'] = str(cine_metadata.TriggerTime_displ)
    
    # ===== BITMAP INFO HEADER =====
    if cine_metadata.biSize is not None:
        tiff_metadata['bi_size'] = int(cine_metadata.biSize)
    
    if cine_metadata.biWidth is not None:
        tiff_metadata['bi_width'] = int(cine_metadata.biWidth)
    
    if cine_metadata.biHeight is not None:
        tiff_metadata['bi_height'] = int(cine_metadata.biHeight)
    
    if cine_metadata.biPlanes is not None:
        tiff_metadata['bi_planes'] = int(cine_metadata.biPlanes)
    
    if cine_metadata.biBitCount is not None:
        tiff_metadata['bi_bit_count'] = int(cine_metadata.biBitCount)
    
    if cine_metadata.biCompression is not None:
        tiff_metadata['bi_compression'] = str(cine_metadata.biCompression)
    
    if cine_metadata.biSizeImage is not None:
        tiff_metadata['bi_size_image'] = int(cine_metadata.biSizeImage)
    
    if cine_metadata.biXPelsPerMeter is not None:
        tiff_metadata['bi_x_pels_per_meter'] = int(cine_metadata.biXPelsPerMeter)
    
    if cine_metadata.biYPelsPerMeter is not None:
        tiff_metadata['bi_y_pels_per_meter'] = int(cine_metadata.biYPelsPerMeter)
    
    if cine_metadata.biClrUsed is not None:
        tiff_metadata['bi_clr_used'] = int(cine_metadata.biClrUsed)
    
    if cine_metadata.biClrImportant is not None:
        tiff_metadata['bi_clr_important'] = int(cine_metadata.biClrImportant)
    
    # ===== SETUP INFO =====
    if cine_metadata.TrigFrame is not None:
        tiff_metadata['trig_frame'] = int(cine_metadata.TrigFrame)
    
    if cine_metadata.Mark is not None:
        tiff_metadata['mark'] = str(cine_metadata.Mark)
    
    if cine_metadata.Length is not None:
        tiff_metadata['length'] = int(cine_metadata.Length)
    
    if cine_metadata.SigOption is not None:
        tiff_metadata['sig_option'] = int(cine_metadata.SigOption)
    
    if cine_metadata.BinChannels is not None:
        tiff_metadata['bin_channels'] = int(cine_metadata.BinChannels)
    
    if cine_metadata.SamplesPerImage is not None:
        tiff_metadata['samples_per_image'] = int(cine_metadata.SamplesPerImage)
    
    if cine_metadata.BinName and len(cine_metadata.BinName) > 0:
        tiff_metadata['bin_names'] = [str(name) for name in cine_metadata.BinName]
    
    if cine_metadata.AnaOption is not None:
        tiff_metadata['ana_option'] = int(cine_metadata.AnaOption)
    
    if cine_metadata.AnaChannels is not None:
        tiff_metadata['ana_channels'] = int(cine_metadata.AnaChannels)
    
    if cine_metadata.AnaBoard is not None:
        tiff_metadata['ana_board'] = str(cine_metadata.AnaBoard)
    
    if cine_metadata.ChOption and len(cine_metadata.ChOption) > 0:
        tiff_metadata['ch_options'] = [int(opt) for opt in cine_metadata.ChOption]
    
    if cine_metadata.AnaGain and len(cine_metadata.AnaGain) > 0:
        tiff_metadata['ana_gains'] = [float(g) for g in cine_metadata.AnaGain]
    
    if cine_metadata.AnaUnit and len(cine_metadata.AnaUnit) > 0:
        tiff_metadata['ana_units'] = [str(u) for u in cine_metadata.AnaUnit]
    
    if cine_metadata.AnaName and len(cine_metadata.AnaName) > 0:
        tiff_metadata['ana_names'] = [str(name) for name in cine_metadata.AnaName]
    
    if cine_metadata.lFirstImage is not None:
        tiff_metadata['l_first_image'] = int(cine_metadata.lFirstImage)
    
    if cine_metadata.dwImageCount is not None:
        tiff_metadata['dw_image_count'] = int(cine_metadata.dwImageCount)
    
    if cine_metadata.nQFactor is not None:
        tiff_metadata['q_factor'] = int(cine_metadata.nQFactor)
    
    if cine_metadata.wCineFileType is not None:
        tiff_metadata['cine_file_type'] = int(cine_metadata.wCineFileType)
    
    if cine_metadata.szCinePath and len(cine_metadata.szCinePath) > 0:
        tiff_metadata['cine_paths'] = [str(p) for p in cine_metadata.szCinePath]
    
    # ===== ACQUISITION PARAMETERS =====
    if cine_metadata.ImWidth is not None:
        tiff_metadata['im_width'] = int(cine_metadata.ImWidth)
    
    if cine_metadata.ImHeight is not None:
        tiff_metadata['im_height'] = int(cine_metadata.ImHeight)
    
    if cine_metadata.Serial is not None:
        tiff_metadata['serial'] = str(cine_metadata.Serial)
    
    if cine_metadata.AutoExposure is not None:
        tiff_metadata['auto_exposure'] = bool(cine_metadata.AutoExposure)
    
    if cine_metadata.bFlipH is not None:
        tiff_metadata['flip_horizontal'] = bool(cine_metadata.bFlipH)
    
    if cine_metadata.bFlipV is not None:
        tiff_metadata['flip_vertical'] = bool(cine_metadata.bFlipV)
    
    if cine_metadata.Grid is not None:
        tiff_metadata['grid'] = str(cine_metadata.Grid)
    
    if cine_metadata.FrameRate is not None:
        tiff_metadata['frame_rate'] = float(cine_metadata.FrameRate)
    
    if cine_metadata.PostTrigger is not None:
        tiff_metadata['post_trigger'] = float(cine_metadata.PostTrigger)
    
    if cine_metadata.bEnableColor is not None:
        tiff_metadata['enable_color'] = bool(cine_metadata.bEnableColor)
    
    if cine_metadata.CameraVersion is not None:
        tiff_metadata['camera_version'] = str(cine_metadata.CameraVersion)
    
    if cine_metadata.FirmwareVersion is not None:
        tiff_metadata['firmware_version'] = str(cine_metadata.FirmwareVersion)
    
    if cine_metadata.SoftwareVersion is not None:
        tiff_metadata['software_version'] = str(cine_metadata.SoftwareVersion)
    
    if cine_metadata.RecordingTimeZone is not None:
        tiff_metadata['recording_timezone'] = str(cine_metadata.RecordingTimeZone)
    
    if cine_metadata.CFA is not None:
        tiff_metadata['color_filter_array'] = str(cine_metadata.CFA)
    
    # ===== IMAGE PROCESSING =====
    if cine_metadata.AutoExpLevel is not None:
        tiff_metadata['auto_exp_level'] = int(cine_metadata.AutoExpLevel)
    
    if cine_metadata.AutoExpRect and len(cine_metadata.AutoExpRect) > 0:
        tiff_metadata['auto_exp_rect'] = [int(v) for v in cine_metadata.AutoExpRect]
    
    if cine_metadata.WBGain_R and len(cine_metadata.WBGain_R) > 0:
        tiff_metadata['wb_gain_r'] = [float(g) for g in cine_metadata.WBGain_R]
    
    if cine_metadata.WBGain_B and len(cine_metadata.WBGain_B) > 0:
        tiff_metadata['wb_gain_b'] = [float(g) for g in cine_metadata.WBGain_B]
    
    if cine_metadata.WBGain and len(cine_metadata.WBGain) > 0:
        tiff_metadata['wb_gain'] = [float(g) for g in cine_metadata.WBGain]
    
    if cine_metadata.RealBPP is not None:
        tiff_metadata['real_bpp'] = float(cine_metadata.RealBPP)
    
    if cine_metadata.Rotate is not None:
        tiff_metadata['rotate'] = int(cine_metadata.Rotate)
    
    if cine_metadata.WBView is not None:
        tiff_metadata['wb_view'] = str(cine_metadata.WBView)
    
    if cine_metadata.FilterCode is not None:
        tiff_metadata['filter_code'] = str(cine_metadata.FilterCode)
    
    if cine_metadata.FilterParam is not None:
        tiff_metadata['filter_param'] = str(cine_metadata.FilterParam)
    
    if cine_metadata.ImFilter is not None:
        tiff_metadata['im_filter'] = str(cine_metadata.ImFilter)
    
    if cine_metadata.BlackCalSVer is not None and cine_metadata.BlackCalSVer != 0:
        tiff_metadata['black_cal_sver'] = int(cine_metadata.BlackCalSVer)
    
    if cine_metadata.WhiteCalSVer is not None and cine_metadata.WhiteCalSVer != 0:
        tiff_metadata['white_cal_sver'] = int(cine_metadata.WhiteCalSVer)
    
    if cine_metadata.GrayCalSVer is not None and cine_metadata.GrayCalSVer != 0:
        tiff_metadata['gray_cal_sver'] = int(cine_metadata.GrayCalSVer)
    
    if cine_metadata.bStampTime is not None:
        tiff_metadata['stamp_time'] = bool(cine_metadata.bStampTime)
    
    if cine_metadata.SoundDest is not None:
        tiff_metadata['sound_dest'] = str(cine_metadata.SoundDest)
    
    if cine_metadata.MCCnt is not None:
        tiff_metadata['mc_cnt'] = int(cine_metadata.MCCnt)
    
    if cine_metadata.CICalib is not None:
        tiff_metadata['ci_calib'] = str(cine_metadata.CICalib)
    
    if cine_metadata.CalibWidth is not None:
        tiff_metadata['calib_width'] = int(cine_metadata.CalibWidth)
    
    if cine_metadata.CalibHeight is not None:
        tiff_metadata['calib_height'] = int(cine_metadata.CalibHeight)
    
    if cine_metadata.CalibRate is not None:
        tiff_metadata['calib_rate'] = float(cine_metadata.CalibRate)
    
    if cine_metadata.CalibExp is not None:
        tiff_metadata['calib_exp'] = float(cine_metadata.CalibExp)
    
    if cine_metadata.CalibEDR is not None:
        tiff_metadata['calib_edr'] = str(cine_metadata.CalibEDR)
    
    if cine_metadata.CalibTemp is not None and cine_metadata.CalibTemp != 0:
        tiff_metadata['calib_temp'] = float(cine_metadata.CalibTemp)
    
    if cine_metadata.HeadSerial is not None:
        tiff_metadata['head_serial'] = str(cine_metadata.HeadSerial)
    
    if cine_metadata.RangeCode is not None:
        tiff_metadata['range_code'] = str(cine_metadata.RangeCode)
    
    if cine_metadata.RangeSize is not None:
        tiff_metadata['range_size'] = int(cine_metadata.RangeSize)
    
    if cine_metadata.Decimation is not None:
        tiff_metadata['decimation'] = int(cine_metadata.Decimation)
    
    if cine_metadata.MasterSerial is not None:
        tiff_metadata['master_serial'] = str(cine_metadata.MasterSerial)
    
    if cine_metadata.Sensor is not None:
        tiff_metadata['sensor'] = str(cine_metadata.Sensor)
    
    if cine_metadata.ExposureTime is not None:
        tiff_metadata['exposure_time'] = float(cine_metadata.ExposureTime)
    
    if cine_metadata.EDR is not None:
        tiff_metadata['edr'] = str(cine_metadata.EDR)
    
    if cine_metadata.FrameDelay is not None:
        tiff_metadata['frame_delay'] = float(cine_metadata.FrameDelay)
    
    if cine_metadata.ImPosXAcq is not None:
        tiff_metadata['im_pos_x_acq'] = int(cine_metadata.ImPosXAcq)
    
    if cine_metadata.ImPosYAcq is not None:
        tiff_metadata['im_pos_y_acq'] = int(cine_metadata.ImPosYAcq)
    
    if cine_metadata.ImWidthAcq is not None:
        tiff_metadata['im_width_acq'] = int(cine_metadata.ImWidthAcq)
    
    if cine_metadata.ImHeightAcq is not None:
        tiff_metadata['im_height_acq'] = int(cine_metadata.ImHeightAcq)
    
    if cine_metadata.RisingEdge is not None:
        tiff_metadata['rising_edge'] = bool(cine_metadata.RisingEdge)
    
    if cine_metadata.FilterTime is not None:
        tiff_metadata['filter_time'] = float(cine_metadata.FilterTime)
    
    if cine_metadata.LongReady is not None:
        tiff_metadata['long_ready'] = bool(cine_metadata.LongReady)
    
    if cine_metadata.PIV is not None:
        tiff_metadata['piv'] = str(cine_metadata.PIV)
    
    if cine_metadata.bMetaWB is not None:
        tiff_metadata['meta_wb'] = bool(cine_metadata.bMetaWB)
    
    if cine_metadata.BlackLevel is not None:
        tiff_metadata['black_level'] = float(cine_metadata.BlackLevel)
    
    if cine_metadata.WhiteLevel is not None:
        tiff_metadata['white_level'] = float(cine_metadata.WhiteLevel)
    
    if cine_metadata.Bright is not None:
        tiff_metadata['brightness'] = float(cine_metadata.Bright)
    
    if cine_metadata.Contrast is not None:
        tiff_metadata['contrast'] = float(cine_metadata.Contrast)
    
    if cine_metadata.Saturation is not None:
        tiff_metadata['saturation'] = float(cine_metadata.Saturation)
    
    if cine_metadata.Hue is not None:
        tiff_metadata['hue'] = float(cine_metadata.Hue)
    
    if cine_metadata.Gamma is not None:
        tiff_metadata['gamma'] = float(cine_metadata.Gamma)
    
    if cine_metadata.fGammaR is not None:
        tiff_metadata['gamma_r'] = float(cine_metadata.fGammaR)
    
    if cine_metadata.fGammaB is not None:
        tiff_metadata['gamma_b'] = float(cine_metadata.fGammaB)
    
    if cine_metadata.fFlare is not None:
        tiff_metadata['flare'] = float(cine_metadata.fFlare)
    
    if cine_metadata.fPedestalR is not None:
        tiff_metadata['pedestal_r'] = float(cine_metadata.fPedestalR)
    
    if cine_metadata.fPedestalG is not None:
        tiff_metadata['pedestal_g'] = float(cine_metadata.fPedestalG)
    
    if cine_metadata.fPedestalB is not None:
        tiff_metadata['pedestal_b'] = float(cine_metadata.fPedestalB)
    
    if cine_metadata.fChroma is not None:
        tiff_metadata['chroma'] = float(cine_metadata.fChroma)
    
    # if cine_metadata.fTone is not None:
    #     tiff_metadata['tone'] = cine_metadata.fTone # Not JSON serializable
    
    if cine_metadata.TonePoints is not None:
        tiff_metadata['tone_points'] = str(cine_metadata.TonePoints)
    
    if cine_metadata.UserMatrixLabel is not None:
        tiff_metadata['user_matrix_label'] = str(cine_metadata.UserMatrixLabel)
    
    if cine_metadata.EnableMatrices is not None:
        tiff_metadata['enable_matrices'] = bool(cine_metadata.EnableMatrices)
    
    if cine_metadata.fUserMatrix is not None:
        tiff_metadata['user_matrix'] = str(cine_metadata.fUserMatrix)
    
    if cine_metadata.EnableCrop is not None:
        tiff_metadata['enable_crop'] = bool(cine_metadata.EnableCrop)
    
    if cine_metadata.CropRect and len(cine_metadata.CropRect) > 0:
        tiff_metadata['crop_rect'] = [int(v) for v in cine_metadata.CropRect]
    
    if cine_metadata.EnableResample is not None:
        tiff_metadata['enable_resample'] = bool(cine_metadata.EnableResample)
    
    if cine_metadata.ResampleWidth is not None:
        tiff_metadata['resample_width'] = int(cine_metadata.ResampleWidth)
    
    if cine_metadata.ResampleHeight is not None:
        tiff_metadata['resample_height'] = int(cine_metadata.ResampleHeight)
    
    if cine_metadata.fGain16_8 is not None:
        tiff_metadata['gain_16_8'] = float(cine_metadata.fGain16_8)
    
    if cine_metadata.TrigTC is not None:
        tiff_metadata['trig_tc'] = str(cine_metadata.TrigTC)
    
    if cine_metadata.fPbRate is not None:
        tiff_metadata['pb_rate'] = float(cine_metadata.fPbRate)
    
    if cine_metadata.fTcRate is not None:
        tiff_metadata['tc_rate'] = float(cine_metadata.fTcRate)
    
    if cine_metadata.fGainR is not None:
        tiff_metadata['gain_r'] = float(cine_metadata.fGainR)
    
    if cine_metadata.fGainG is not None:
        tiff_metadata['gain_g'] = float(cine_metadata.fGainG)
    
    if cine_metadata.fGainB is not None:
        tiff_metadata['gain_b'] = float(cine_metadata.fGainB)
    
    if cine_metadata.cmCalib and len(cine_metadata.cmCalib) > 0:
        tiff_metadata['cm_calib'] = [float(v) for v in cine_metadata.cmCalib]
    
    if cine_metadata.fToe is not None:
        tiff_metadata['toe'] = float(cine_metadata.fToe)
    
    if cine_metadata.CameraModel is not None:
        tiff_metadata['camera_model'] = str(cine_metadata.CameraModel)
    
    if cine_metadata.fWBTemp is not None:
        tiff_metadata['wb_temperature'] = float(cine_metadata.fWBTemp)
    
    if cine_metadata.fWBCc is not None:
        tiff_metadata['wb_cc'] = float(cine_metadata.fWBCc)
    
    if cine_metadata.WBType is not None:
        tiff_metadata['wb_type'] = str(cine_metadata.WBType)
    
    if cine_metadata.fDecimation is not None:
        tiff_metadata['f_decimation'] = float(cine_metadata.fDecimation)
    
    if cine_metadata.SensorMode is not None:
        tiff_metadata['sensor_mode'] = str(cine_metadata.SensorMode)
    
    if cine_metadata.UndecFirst is not None:
        tiff_metadata['undec_first'] = bool(cine_metadata.UndecFirst)
    
    if cine_metadata.SupportsBinning is not None:
        tiff_metadata['supports_binning'] = bool(cine_metadata.SupportsBinning)
    
    if cine_metadata.UvSensor is not None:
        tiff_metadata['uv_sensor'] = bool(cine_metadata.UvSensor)
    
    if cine_metadata.AnaDaqDescription is not None:
        tiff_metadata['ana_daq_description'] = str(cine_metadata.AnaDaqDescription)
    
    if cine_metadata.BinDaqDescription is not None:
        tiff_metadata['bin_daq_description'] = str(cine_metadata.BinDaqDescription)
    
    if cine_metadata.DaqOptions is not None:
        tiff_metadata['daq_options'] = str(cine_metadata.DaqOptions)
    
    if cine_metadata.DecimatedFrameRate is not None:
        tiff_metadata['decimated_frame_rate'] = float(cine_metadata.DecimatedFrameRate)
    
    # ===== LUT (Look-Up Table) =====
    # Note: LUT_P10 is a large numpy array; only include if specifically needed
    # Uncomment the line below if you want to include it
    # if cine_metadata.LUT_P10 is not None:
    #     tiff_metadata['lut_p10'] = cine_metadata.LUT_P10.tolist()
    
    return tiff_metadata

def write_metadata(metadata, output_path=None):
    """
    Write OME-TIFF metadata to a CSV file.
    
    Args:
        metadata: Dictionary containing OME-TIFF metadata (from cine_metadata_to_tiff_metadata)
        output_path: (Optional) Path to save the CSV file. If None, uses metadata.csv in current directory.
    """
    
    if output_path is None:
        output_path = "metadata.csv"
    
    # Flatten the nested metadata dictionary
    flat_metadata = _flatten_metadata(metadata)
    
    # Write to CSV
    with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write header
        writer.writerow(['Key', 'Value'])
        
        # Write data rows
        for key, value in sorted(flat_metadata.items()):
            writer.writerow([key, value])
    
    print(f"Metadata written to {output_path}")

def _flatten_metadata(metadata_dict, parent_key='', separator='.'):
    """
    Flatten nested metadata dictionary with dot notation.
    
    Args:
        metadata_dict: Nested dictionary
        parent_key: Prefix for nested keys
        separator: Separator character (default: '.')
        
    Returns:
        dict: Flattened dictionary with dot-notation keys
    """
    flat_dict = {}
    
    for key, value in metadata_dict.items():
        new_key = f"{parent_key}{separator}{key}" if parent_key else key
        
        if isinstance(value, dict):
            flat_dict.update(_flatten_metadata(value, new_key, separator))
        elif isinstance(value, list):
            # Convert lists to comma-separated strings
            flat_dict[new_key] = ', '.join(str(v) for v in value)
        else:
            flat_dict[new_key] = value
    
    return flat_dict

if __name__ == "__main__":

    path = "/home/zorrilla/Work/OngoingProjects/EPFL_Biophysics/Haematococcus pluvialis/Katerina/20261006_red_cells/"
    
    cine_path = path + "20261006_red_cells03.cine"
    metadata = cr.read_metadata(cine_path)
    metadata, images, timestamps = cr.read(cine_path, start = metadata.FirstImageNo, count = metadata.ImageCount - 1800)
    # images: List of numpy arrays, each representing an image
    # timestamps: numpy array of timestamps for each image

    # Convert CINE MetaData to dictionary
    metadata_dict = cine_metadata_to_dict_metadata(metadata)

    tiff_path = path + "20261006_red_cells03.ome.tif"
    imwrite(
        tiff_path, 
        images, 
        bigtiff=False,
        photometric='minisblack',
        metadata=metadata_dict,
        )
    
    # Write metadata to CSV
    csv_path = path + "20261006_red_cells03_metadata.csv"
    write_metadata(metadata_dict, output_path=csv_path)