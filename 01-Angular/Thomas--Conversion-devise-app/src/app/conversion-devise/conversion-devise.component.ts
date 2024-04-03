import { Component, OnInit } from '@angular/core';
import {NgForm} from "@angular/forms";
import {HttpClient} from "@angular/common/http";
import {DevisesService} from "../services/mock-api-devise";
import {Devise} from "../models/devise.model";

@Component({
  selector: 'app-conversion-devise',
  templateUrl: './conversion-devise.component.html',
  styleUrls: ['./conversion-devise.component.css']
})
export class ConversionDeviseComponent implements OnInit {

  public defaultBaseCurrencySign: string = "EUR";
  public defaultTargetCurrencySign: string = "USD";
  public result!: string;
  private apiKey: string = "f265c640-83fc-11ec-9dd2-a70b48bbcef3";
  private url: string = "https://freecurrencyapi.net/api/v2/latest?apikey=" + this.apiKey
  public currencies: Array<Devise> = DevisesService;

  constructor(private http: HttpClient) {}

  ngOnInit(): void {}

  onSubmit(form: NgForm){
    const fromCurrency = [form.value['base-currency'], form.value['base-currency-sign']]
    const toCurrency = form.value['target-currency-sign'];
    if (toCurrency == fromCurrency[1]){
      this.result = fromCurrency[0].toString();
      return;
    }
    const url = this.url + "&base_currency=" + fromCurrency[1]
    this.http
      .get<any>(url)
      .subscribe({
        next: (response) => {
          const multiplier = response['data'][toCurrency];
          const localCurrency = this.currencies.find(c =>  c.name == toCurrency );
          if (localCurrency) {
            localCurrency.multiplier = multiplier;
          }
          this.result = (fromCurrency[0] * multiplier).toString();
        },
        error: (e) => {console.log("Erreur ! " + e);}
      })
  }
}
