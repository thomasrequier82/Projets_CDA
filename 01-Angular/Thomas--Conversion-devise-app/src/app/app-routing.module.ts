import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { DeviseListComponent } from './devise-list/devise-list.component';
import {SingleFaceSnapComponent} from "./single-devise-snap/single-face-snap.component";
import { LandingPageComponent } from './landing-page/landing-page.component';
import {ConversionDeviseComponent} from "./conversion-devise/conversion-devise.component";

const routes: Routes = [
  { path: 'facesnaps/:id', component: SingleFaceSnapComponent },
  { path: 'facesnaps', component: DeviseListComponent },
  { path: "currency", component:ConversionDeviseComponent},
  { path: '', component: LandingPageComponent }
];


@NgModule({
  imports: [
    RouterModule.forRoot(routes),

  ],
  exports: [
    RouterModule,
      ]
})
export class AppRoutingModule {}
