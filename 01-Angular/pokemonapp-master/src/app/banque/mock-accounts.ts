import {Account} from "./Account.model";

export const ACCOUNTS: Array<Account> = [
  {
    id: 1,
    name: "Compte courant",
    owner: ["John", "Doe"],
    money: 6000
  },
  {
    id: 2,
    name: "Epargne",
    owner: ["John", "Doe"],
    money: 15000
  }
];
