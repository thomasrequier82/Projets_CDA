import { Component, OnInit } from '@angular/core';
import { Devise } from '../models/devise.model';
import { DevisesService } from '../services/mock-api-devise';

@Component({
  selector: 'app-face-snap-list',
  templateUrl: './devise-list.component.html',
  styleUrls: ['./devise-list.component.scss']
})


export class DeviseListComponent implements OnInit {

  faceSnaps!: Devise[];

  constructor(private faceSnapsService: DevisesService) { }

  ngOnInit(): void {

    this.faceSnaps = this.faceSnapsService.getAllDevises();
  }
  }

