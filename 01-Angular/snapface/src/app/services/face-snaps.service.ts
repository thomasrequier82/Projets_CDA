import { Injectable } from '@angular/core';
import { FaceSnap } from '../models/face-snap.model'

@Injectable({
  providedIn: 'root'
})
export class FaceSnapsService {
  faceSnaps: FaceSnap[] = [
    {
      id: 1,
      title: 'Archibald',
      description: 'Mon meilleur ami depuis tout petit !',
      imageUrl: 'https://cdn.pixabay.com/photo/2015/05/31/16/03/teddy-bear-792273_1280.jpg',
      createdDate: new Date(),
      snaps: 4,
      location: 'Paris'
    },
    {
      id: 2,
      title: 'Fénéant dans le canapé',
      description: 'Occupation du dimanche aprèm',
      imageUrl: 'https://cdn-images-1.medium.com/max/2000/1*KiC1gf3x3Ia_2PBYqfkLBg.jpeg',
      createdDate: new Date(),
      snaps: 52,
      location: 'Rennes'
    },
    {
      id: 3,
      title: 'Anniversaire',
      description: 'Carte anniversaire de la star',
      imageUrl: 'https://dk2wbmtb9x9n8.cloudfront.net/voeux/6/653/6538-Anniversaire%20de%20la%20star_medium.gif',
      createdDate: new Date(),
      snaps: 66,
      location: 'Londres'
    }
    // vos FaceSnap ici
  ];

  getAllFaceSnaps(): FaceSnap[] {
    return this.faceSnaps;
  }
  getFaceSnapById(faceSnapId: number): FaceSnap {
    const faceSnap = this.faceSnaps.find(faceSnap => faceSnap.id === faceSnapId);
    if (!faceSnap) {
      throw new Error('FaceSnap not found!');
    } else {
      return faceSnap;
    }
  }
  snapFaceSnapById(faceSnapId: number, snapType: 'snap' | 'unsnap'): void {
    const faceSnap = this.getFaceSnapById(faceSnapId);
    snapType === 'snap' ? faceSnap.snaps++ : faceSnap.snaps--;
  }

}
