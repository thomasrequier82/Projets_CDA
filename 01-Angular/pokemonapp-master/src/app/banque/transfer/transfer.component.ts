import {Component, Input, OnInit} from '@angular/core';
import {ACCOUNTS} from "../mock-accounts";
import {Account} from "../Account.model";
import {Router} from "@angular/router";

@Component({
  selector: 'app-transfer',
  templateUrl: './transfer.component.html',
  styleUrls: ['./transfer.component.css']
})
export class TransferComponent implements OnInit {

  public accounts: Array<Account> = ACCOUNTS;
  public fromAccount!: Account;
  public toAccount!: Account;

  @Input()
  public money!: number;

  constructor(private router: Router) { }

  ngOnInit(): void {
  }

  onClickFrom(account: Account) {
    this.fromAccount = account;
  }

  onClickTo(account: Account) {
    this.toAccount = account;
  }

  onSubmit(){
    if (this.fromAccount && this.toAccount && this.money && this.money > 0) {
      this.fromAccount.money -= this.money;
      this.toAccount.money += this.money;
      this.router.navigate(["/banque"]).then();
    }
  }
}
