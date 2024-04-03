import { Component, OnInit, Input } from '@angular/core';
import { Devise } from '../models/devise.model';
import { FaceSnapsService } from '../services/mock-api-devise';
import {Router} from "@angular/router";

@Component({
  selector: 'app-face-snap',
  templateUrl: './devise.component.html',
  styleUrls: ['./devise.component.scss']
})
export class DeviseComponent implements OnInit {
  @Input() faceSnap!: Devise;

  buttonText!: string;

  constructor(private faceSnapsService: FaceSnapsService,
              private router: Router) {}

  ngOnInit() {
    this.buttonText = 'Oh Snap !!';
  }
  onSnap() {
    if (this.buttonText === 'Oh Snap!') {
      this.faceSnapsService.snapFaceSnapById(this.faceSnap.id,'snap');
      this.buttonText = 'Oops, unSnap!';
    } else {
      this.faceSnapsService.snapFaceSnapById(this.faceSnap.id,'unsnap')
      this.buttonText = 'Oh Snap!'
    }
  }

}
