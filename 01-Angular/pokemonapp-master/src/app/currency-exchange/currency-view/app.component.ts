import { Component, OnInit } from '@angular/core';
import {NgForm} from "@angular/forms";
import {HttpClient} from "@angular/common/http";
import {CURRENCIES} from "../mock-api";
import {Currency} from "../Currency.model";

@Component({
  selector: 'currency-view',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class CurrencyAppComponent implements OnInit {

  public defaultBaseCurrencySign: string = "EUR";
  public defaultTargetCurrencySign: string = "USD";
  public result!: string;
  public currencies: Array<Currency> = CURRENCIES;

  private apiKey: string = "f265c640-83fc-11ec-9dd2-a70b48bbcef3";
  private url: string = "https://freecurrencyapi.net/api/v2/latest?apikey=" + this.apiKey

  constructor(private httpClient: HttpClient) {}

  ngOnInit(): void {}

  onSubmit(form: NgForm){
    const fromCurrency = [form.value['base-currency'], form.value['base-currency-sign']]
    const toCurrency = form.value['target-currency-sign'];
    if (!fromCurrency[0] || toCurrency == fromCurrency[1]) {
      return this.result = fromCurrency[0];
    }
    this.result = "Chargement...";
    const url = this.url + "&base_currency=" + fromCurrency[1]
    this.httpClient
      .get<any>(url)
      .subscribe({
        next: (response) => {
          const multiplier = response['data'][toCurrency];
          this.result = (fromCurrency[0] * multiplier).toString();
          for (let currency of this.currencies) {
            currency.multiplier = response['data'][currency.name];
          }
        },
        error: (e) => console.log("Erreur ! " + e)
      })
  }
}
