from _fsps import fsps

# Because I don't know Fortran all that well, this is how I hack things to
# make sure that my magic numbers are right.
ntfull, nspec, nbands = fsps.get_dims()
assert ntfull == fsps.ntfull2 and nspec == fsps.nspec2 \
        and nbands == fsps.nbands2, \
        "There's a problem with the dimensions in fsps.f95"

bands = ["v", "u", "deep_b", "deep_r", "deep_i", "twomass_j", "twomass_h",
    "twomass_k", "sdss_u", "sdss_g", "sdss_r", "sdss_i", "sdss_z",
    "wfc_f435w", "wfc_f606w", "wfc_f775w", "wfc_f814w", "wfc_f850lp",
    "irac1", "irac2", "irac3", "irac4", "nicmos_f110w", "nicmos_f160w",
    "fors_v", "fors_r", "galex_nuv", "galex_fuv", "wfcam_z", "wfcam_y",
    "wfcam_j", "wfcam_h", "wfcam_k", "b", "r", "i", "b3", "wfpc2_f555w",
    "wfpc2_f814w", "wfc3_f275w"]

def compute(imf_type=0, zmet=1, sfh=0):
    assert imf_type in range(6)
    assert zmet in range(1, 23)
    assert sfh in range(5)

    fsps.compute(imf_type, zmet, sfh)

def get_mag(band):
    return fsps.mags[bands.index(band)]

