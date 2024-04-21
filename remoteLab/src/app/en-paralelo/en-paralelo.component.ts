import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-en-paralelo',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './en-paralelo.component.html',
  styleUrl: './en-paralelo.component.css'
})
export class EnParaleloComponent {
  numRamasEnParalelo = '2ramas';
}
