import { Component, OnInit } from '@angular/core';
import {Account} from "../Account.model";
import {ACCOUNTS} from "../mock-accounts";

@Component({
  selector: 'banque-view',
  templateUrl: './banque-view.component.html',
  styleUrls: ['./banque-view.component.css']
})
export class BanqueAppComponent implements OnInit {

  public accounts: Array<Account> = ACCOUNTS;

  constructor() { }

  ngOnInit(): void {
  }


  getColor(money: number) {
    return money > 0 ? 'green' : 'red';
  }
}
