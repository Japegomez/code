import { NgClass } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-serie-yparalelo',
  standalone: true,
  imports: [FormsModule, NgClass],
  templateUrl: './serie-yparalelo.component.html',
  styleUrl: './serie-yparalelo.component.css'
})
export class SerieYParaleloComponent {
  valorR1: number | undefined;
  isCorrect: boolean = false;

  checkValues() {
    if (this.valorR1 === 100 || this.valorR1 === 300) {
      this.isCorrect = true;
    } else {
      this.isCorrect = false;
    }
  }
}
