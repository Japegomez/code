import { NgClass } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-en-paralelo',
  standalone: true,
  imports: [FormsModule,NgClass],
  templateUrl: './en-paralelo.component.html',
  styleUrl: './en-paralelo.component.css'
})
export class EnParaleloComponent {
  numRamasEnParalelo = '2ramas';

  valorR1: number | undefined;
  valorR2: number | undefined;
  valorR3: number | undefined;
  isCorrect: boolean = false;

  checkValues() {
    if (this.numRamasEnParalelo === '2ramas') {
      if ((this.valorR1 === 100 || this.valorR1 === 300) && (this.valorR2 === 100 || this.valorR2 === 300)) {
        this.isCorrect = true;
      } else {
        this.isCorrect = false;
      }
    } else if (this.numRamasEnParalelo === '3ramas') {
      if ((this.valorR1 === 100 || this.valorR1 === 300) && (this.valorR2 === 100 || this.valorR2 === 300) && (this.valorR3 === 100 || this.valorR3 === 300)) {
        this.isCorrect = true;
      } else {
        this.isCorrect = false;
      }
    }
  }
}
