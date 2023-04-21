import ddosa
from astropy.io import fits


class CheckStep(ddosa.DataAnalysis):
    input_lc=ddosa.ii_lc_extract

    def main(self):
        lc = fits.open(self.input_lc.lightcurve.get_path())[2].data

        m_start = lc['TIME'] < lc['TIME'].min() + 1000/3600/24
        m_end = lc['TIME'] > lc['TIME'].max() - 1000/3600/24

        if lc['RATE'][m_end].mean() > 85:
            print("\033[31mFAIL!\033[0m")
            self.status = "fail"
        else:
            print("\033[32mOK!\033[0m")
            self.status = "success"

