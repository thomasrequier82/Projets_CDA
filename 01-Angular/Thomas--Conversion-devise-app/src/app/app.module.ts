import { LOCALE_ID,DEFAULT_CURRENCY_CODE,NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { DeviseComponent } from './devise-to-convert/devise.component';
import { registerLocaleData } from '@angular/common';
import * as fr from '@angular/common/locales/fr';
import { DeviseListComponent } from './devise-list/devise-list.component';
import { HeaderComponent } from './header/header.component';
import {AppRoutingModule} from "./app-routing.module";
import { LandingPageComponent } from './landing-page/landing-page.component';
import { SingleFaceSnapComponent } from './single-devise-snap/single-face-snap.component';
import { ConversionDeviseComponent } from './conversion-devise/conversion-devise.component';

@NgModule({
  declarations: [
    AppComponent,
    DeviseComponent,
    DeviseListComponent,
    HeaderComponent,
    LandingPageComponent,
    SingleFaceSnapComponent,
    ConversionDeviseComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [
    { provide: LOCALE_ID, useValue: 'fr-FR'},{provide: DEFAULT_CURRENCY_CODE, useValue: 'EUR' }
  ],
  bootstrap: [AppComponent]
})
export class AppModule {
  constructor() {
    registerLocaleData(fr.default);
  }
}
