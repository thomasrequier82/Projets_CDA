import { Injectable } from '@angular/core';
import { Devise } from '../models/devise.model'

@Injectable({
  providedIn: 'root'
})

const data = {
  "JPY": 129.355406,
  "PGK": 3.987047,
  "TJS": 12.78381,
  "XPF": 118.984986,
  "MGA": 4507.192774,
  "AMD": 544.194382,
  "MKD": 61.382637,
  "LAK": 12816.517754,
  "NIO": 40.050217,
  "MNT": 3220.29416,
  "MUR": 49.652,
  "SSP": 483.646848,
  "ALL": 120.875345,
  "NAD": 17.306377,
  "XAF": 655.856583,
  "JMD": 176.05358,
  "BWP": 13.078083,
  "BSD": 1.13232,
  "AFN": 112.450179,
  "BHD": 0.426888,
  "CDF": 2253.975656,
  "PYG": 7956.891549,
  "UGX": 3963.819704,
  "SVC": 9.907593,
  "TTD": 7.633611,
  "NPR": 135.584458,
  "MZN": 71.460936,
  "HNL": 27.663651,
  "BIH": 1.969881,
  "BND": 1.525001,
  "ISK": 143.056015,
  "KHR": 4588.110286,
  "GEL": 3.402622,
  "HTG": 114.395964,
  "MDL": 20.270914,
  "YER": 283.059842,
  "DJF": 201.101488,
  "LTC": 0.009874,
  "EUR": 1,
  "ETH": 0.000408,
  "GBP": 0.836802,
  "JOD": 0.800885,
  "BTC": 0.028987,
  "BGN": 1.955274,
  "AUD": 1.589361,
  "XRP": 1.819851,
  "STD": 24.676933,
  "KMF": 494.605156,
  "GMD": 60.239639,
  "SOS": 651.080348,
  "SCR": 15.366989,
  "CVE": 110.241995,
  "RWF": 1163.913323,
  "FJD": 2.439433,
  "KGS": 96.016871,
  "GNF": 10138.16005,
  "SRD": 23.850967,
  "SLL": 12838.920094,
  "XOF": 660.505254,
  "MWK": 914.797262,
  "ERN": 16.962034,
  "LRD": 171.547013,
  "SZL": 17.306343,
  "GYD": 235.262421,
  "BIF": 2258.598,
  "KYD": 0.934168,
  "MVR": 17.46037,
  "LSL": 17.29194,
  "BOB": 7.711038,
  "GHS": 7.02037,
  "CNY": 7.203213,
  "IRR": 47557.263554,
  "IQD": 1651.52405,
  "PKR": 199.648976,
  "CLP": 906.079793,
  "PHP": 57.777481,
  "EGP": 17.78877,
  "HKD": 8.824766,
  "ILS": 3.578129,
  "SGD": 1.525228,
  "MYR": 4.737635,
  "DKK": 7.438052,
  "ZAR": 17.30127,
  "THB": 37.55931,
  "COP": 4437.063499,
  "AED": 4.158895,
  "TWD": 31.453281,
  "KZT": 490.445129,
  "KRW": 1355.19223,
  "CHF": 1.039744,
  "CAD": 1.433149,
  "MXN": 23.190996,
  "INR": 84.598476,
  "BRL": 5.955569,
  "RUB": 85.850299,
  "IDR": 16254.429333,
  "NOK": 9.922087,
  "TRY": 15.273824,
  "SAR": 4.247996,
  "SEK": 10.39567,
  "NGN": 470.288759,
  "PLN": 4.546277,
  "ARS": 118.781546,
  "DZD": 157.914817,
  "QAR": 4.137823,
  "LYD": 5.215907,
  "DOP": 65.040649,
  "RSD": 117.512116,
  "LBP": 1704.712464,
  "PAB": 1.132332,
  "TND": 3.246682,
  "TMT": 3.951787,
  "TZS": 2612.265716,
  "CRC": 727.06325,
  "ETB": 56.33165,
  "MOP": 9.089191,
  "HRV": 7.592294,
  "URY": 49.708852,
  "GTQ": 8.696261,
  "KES": 128.517619,
  "UZS": 12224.718658,
  "MMK": 2003.64815,
  "CZK": 24.277402,
  "AOA": 595.931236,
  "PEN": 4.389771,
  "RON": 4.944857,
  "VND": 25641.165904,
  "BDT": 97.15363,
  "HUF": 354.552595,
  "UAH": 32.07198,
  "MAD": 10.574358,
  "SYP": 2842.119095,
  "OMR": 0.435833,
  "CUC": 27.175687,
  "BYR": 2.939603,
  "AZN": 1.915089,
  "LKR": 226.147051,
  "SDG": 497.766056,
  "NZD": 1.707018,
  "USD": 1.132298
}

export const CURRENCIES:Array<Devise> = []
for (let [n, m] of Object.entries(data)) {
  CURRENCIES.push({title: n, multiplier: m});
}
CURRENCIES.sort((a,b) => a.title.localeCompare(b.title));

export class DevisesService {
  Devises: Devise[] = [
    {
      id: 1,
      title: 'Archibald',
      description: 'Mon meilleur ami depuis tout petit !',
      imageUrl: 'https://cdn.pixabay.com/photo/2015/05/31/16/03/teddy-bear-792273_1280.jpg',
      createdDate: new Date(),
      snaps: 4,
      multiplier: 1
    },
    {
      id: 2,
      title: 'Fénéant dans le canapé',
      description: 'Occupation du dimanche aprèm',
      imageUrl: 'https://cdn-images-1.medium.com/max/2000/1*KiC1gf3x3Ia_2PBYqfkLBg.jpeg',
      createdDate: new Date(),
      snaps: 52,
      multiplier: 1
    },
    {
      id: 3,
      title: 'Anniversaire',
      description: 'Carte anniversaire de la star',
      imageUrl: 'https://dk2wbmtb9x9n8.cloudfront.net/voeux/6/653/6538-Anniversaire%20de%20la%20star_medium.gif',
      createdDate: new Date(),
      snaps: 66,
      multiplier: 1
    }
    // vos FaceSnap ici
  ];

  getAllDevises(): Devise[] {
    return this.Devises;
  }
  getDeviseById(deviseId: number): Devise {
    const deviseSnap = this.Devises.find(faceSnap => Devise.id === faceSnapId);
    if (!deviseSnap) {
      throw new Error('FaceSnap not found!');
    } else {
      return deviseSnap;
    }
  }
  snapFaceSnapById(faceSnapId: number, snapType: 'snap' | 'unsnap'): void {
    const faceSnap = this.getFaceSnapById(faceSnapId);
    snapType === 'snap' ? faceSnap.snaps++ : faceSnap.snaps--;
  }

}
