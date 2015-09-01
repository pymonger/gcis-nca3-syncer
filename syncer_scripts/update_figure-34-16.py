#!/usr/bin/env python
import os, sys, re, logging, json, requests, argparse
from string import Template

from gcis_clients import GcisClient


log_format = "[%(asctime)s: %(levelname)s/%(funcName)s] %(message)s"
logging.basicConfig(format=log_format, level=logging.INFO)

# disable unverified HTTPS warnings
requests.packages.urllib3.disable_warnings()


def update(url):
    """Updated GCIS for this figure."""

    # get authenticated GCIS client
    gcis = GcisClient(url)

    dataset_id = "nca3-gistemp-r2010"
    href = "/dataset/"
    update_url = "%s%s" % (url, href)
    check_url = "%s%s" % (update_url, dataset_id)
    if requests.get(check_url, verify=False).status_code == 200:
        update_url = check_url
    data = {
            'identifier':dataset_id,
            'description':"The NASA GISS Surface Temperature Analysis (GISTEMP) provides a measure of the changing global surface temperature with monthly resolution for the period since 1880, when a reasonably global distribution of meteorological stations was established. Input data for the analysis, collected by many national meteorological services around the world, is the unadjusted data of the Global Historical Climatology Network (Peterson and Vose, 1997) except that the USHCN station records included were replaced by a later corrected version. These data were augmented by SCAR data from Antarctic stations. Documentation of our analysis is provided by Hansen et al. (1999), with several modifications described by Hansen et al. (2001). The GISS analysis is updated monthly. \n\nThe data is available on an equal area grid. NASA provides code to read it onto a 2x2 grid. They have two smoothing levels available for their updated data: 250km and 1200km smoothing. They make available a land only version and a version which includes the hadISST (post Dec 1981) and NOAA OI V2 for data over the oceans. There ARE missing data values. \n\nThe page at http://data.giss.nasa.gov/gistemp/updates_v3/ provides the list of updates to the data since December 2011. Earlier updates (since August 2003) can be found at http://data.giss.nasa.gov/gistemp/updates/.",
            'spatial_extent': "maximum_latitude: 90.00; minimum_latitude: -90.00; maximum_longitude: 180.00; minimum_longitude: -180.00;",
            'cite_metadata': "Hansen, J., R. Ruedy, M. Sato, and K. Lo, 2010: Global surface temperature change, Rev. Geophys., 48, RG4004, doi:10.1029/2010RG000345",
            'publication_year': 2010,

            'native_id': "Unknown",
            'release_dt': "1981-10-29T00:00:00",
            'version': "N/A",
            'url': "http://data.giss.nasa.gov/gistemp/",
            'name': "GISS Surface Temperature Analysis (GISTEMP)",
            'attributes': "Combined Land-Surface Air and Sea-Surface Water Temperature Anomalies (Land-Ocean Temperature Index, LOTI): -Global-mean monthly, seasonal, and annual means, 1880-present, updated through most recent month -Northern Hemisphere-mean monthly, seasonal, and annual means, 1880-present, updated through most recent month -Southern Hemisphere-mean monthly, seasonal, and annual means, 1880-present, updated through most recent month -Zonal annual means, 1880-present, updated through most recent completed year Means Based on Land-Surface Air Temperature Anomalies Only (Meteorological Station Data, dTs): -Global-mean monthly, seasonal, and annual means, 1880-present, updated through most recent month -Northern Hemisphere-mean monthly, seasonal, and annual means, 1880-present, updated through most recent month -Southern Hemisphere-mean monthly, seasonal, and annual means, 1880-present, updated through most recent month -Zonal annual means, 1880-present, updated through most recent complete calendar year",
            'temporal_extent': "1880-01-01T00:00:00 2012-12-31T23:59:59",
            }
    r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
    r.raise_for_status()


    organization_id = "climatic-research-unit"
    href = "/organization/"
    update_url = "%s%s"%(url,href)
    check_url = "%s%s"%(update_url, organization_id)
    data = {
            'country_code': "UK",
            'name': "Climatic Research Unit at the University of East Anglia",
            'url': "http://www.cru.uea.ac.uk/",
            'identifier': organization_id,
            'organization_type_identifier': "research",
    }

    if requests.get(check_url, verify=False).status_code == 200:
        update_url = check_url
    r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
    r.raise_for_status()

    #contributing agency

    dataset_id = "nca3-hadcrut4-v4_1_1_0"
    href = "/dataset/"
    update_url = "%s%s"%(url, href)
    check_url = "%s%s" %(update_url, dataset_id)
    if requests.get(check_url, verify=False).status_code == 200:
        update_url = check_url
    data = {
            'version': "4.1.1.0",
            'publication_year': 2012,
            'url': "http://www.metoffice.gov.uk/hadobs/hadcrut4/data/current/download.html",
            'description':"HadCRUT4 is a gridded dataset of global historical surface temperature anomalies relative to a 1961-1990 reference period. Data are available for each month since January 1850, on a 5 degree grid. The dataset is a collaborative product of the Met Office Hadley Centre and the Climatic Research Unit at the University of East Anglia. The gridded data are a blend of the CRUTEM4 land-surface air temperature dataset and the HadSST3 sea-surface temperature (SST) dataset. The dataset is presented as an ensemble of 100 dataset realisations that sample the distribution of uncertainty in the global temperature record given current understanding of non-climatic factors affecting near-surface temperature observations. This ensemble approach allows characterisation of spatially and temporally correlated uncertainty structure in the gridded data, for example arising from uncertainties in methods used to account for changes in SST measurement practices, homogenisation of land station records and the potential impacts of urbanisation. The HadCRUT4 data are neither interpolated nor variance adjusted.",
            'release_dt': "2012-10-29T00:00:00",
            'native_id': "Unknown",
            'spatial_extent': "maximum_latitude: 90.00; minimum_latitude: -90.00; maximum_longitude: 180.00; minimum_longitude: -180.00;",
            'cite_metadata': "Morice, C.P., J.J. Kennedy, N.A. Rayner, and P.D. Jones, 2012: Quantifying uncertainties in global and regional temperature change using an ensemble of observational estimates: The HadCRUT4 data set. J. Geophys. Res., 117, D08101, doi: 10.1029/2011JD017187.",
            'identifier': dataset_id,
            'attributes': "Global historical surface temperature anomalies relative to a 1961-1990 reference period.",
            'temporal_extent': "1850-01-01T00:00:00 2012-12-31T23:59:59",
            'name': "HadCRUT4",
            }
    r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
    r.raise_for_status()
    href = "/dataset/contributors/%s"%dataset_id
    update_url = "%s%s" % (url, href)
    ds_conts = [
            {
                'role':'contributing_agency',
                'organization_identifier':'climatic-research-unit',
            },
            {
                'role':'contributing_agency',
                'organization_identifier':'university-east-anglia',
            },
            {
                'role':'contributing_agency',
                'organization_identifier':'met-office-hadley-centre'
            }
    ]
    for data in ds_conts:
        r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
        r.raise_for_status()



    dataset_id = "nca3-mlost"
    href = "/dataset/"
    update_url = "%s%s"%(url,href)
    check_url = "%s%s"%(update_url, dataset_id)
    if requests.get(check_url, verify=False).status_code == 200:
        update_url = check_url
    data = {
        'release_dt': "2005-10-20T00:00:00",
        'description': "The merged land air and sea surface temperature anomaly analysis is based on data from the Global Historical Climatology Network (GHCN) of land temperatures and the International Comprehensive Ocean-Atmosphere Data Set (ICOADS) of Sea Surface Temperature (SST) data. Temperature anomalies with respect to 1961-1990 are analyzed separately. The analyzed monthly temperature anomalies are then merged to form the global analysis. More dataset information can be found at NCDC's Global Surface Temperature Anomaly webpage. This is the dataset NOAA uses for global temperature monitoring. The data has been changed. See the NCDC doc more for details. Basically, Land surface temperatures are available from the Global Historical Climate Network (GHCN). Sea surface temperatures are determined using the extended reconstructed sea surface temperature (ERSST) analysis. ERSST uses the most recently available International Comprehensive Ocean-Atmosphere Data Set (ICOADS) and statistical methods that allow stable reconstruction using sparse data. The monthly analysis begins January 1854, but due to very sparse data, no global averages are computed before 1880. With more observations after 1880, the signal is stronger and more consistent over time. The ERSST version is now 3b.",
        'version': "3.5.3",
        'url': "http://www.esrl.noaa.gov/psd/data/gridded/data.mlost.html",
        'cite_metadata': "Smith, T. M., et al. (2008), Improvements to NOAA's Historical Merged Land-Ocean Surface Temperature Analysis (1880-2006), J. Climate, 21, 2283-2293.",
        'spatial_extent': "maximum_latitude: 87.5; minimum_latitude: -87.5; maximum_longitude: 177.5; minimum_longitude: -177.5;",
        'publication_year': 2008,
        'native_id': "Unknown",
        'temporal_extent': "1880-01-01T00:00:00 2013-07-31T23:59:59",
        'identifier': dataset_id,
        'attributes': "Monthly Anomalies of air temperature from the GHCN and the NOAAERSST V3b dataset.",
        'name': "NOAA Merged Land-Ocean Surface Temperature Analysis (MLOST)",
    }
    r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
    r.raise_for_status()
    href = "/dataset/contributors/%s"%dataset_id
    update_url = "%s%s" %(url, href)
    ds_conts = [
#        {
            #'role':'data_producer',
#            'person_id':4451,
#        },
        {
            'role':'data_producer',
            'organization_identifier':'earth-system-research-laboratory',
        }
    ]
    for data in ds_conts:
        r = gcis.s.post(update_url, data=json.dumps(data), verify=False)
        r.raise_for_status()


if __name__ == "__main__":
    desc = "Updated Figure 34.16: Observed Change in Global Average Temperature"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('url', help="GCIS url")
    args = parser.parse_args()
    update(args.url)
