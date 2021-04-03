def test_download_data():
    import os

    wsi_url = 'https://data.kitware.com/api/v1/file/5899dd6d8d777f07219fcb23/download'
    wsi_path = 'TCGA-02-0010-01Z-00-DX4.07de2e55-a8fe-40ee-9e98-bcb78050b9f7.svs'

    if not os.path.isfile(wsi_path):
        return os.system(f'curl -OJ {wsi_url}') == 0
    return True


def test_load_wsi_and_plot_hist():
    return True
