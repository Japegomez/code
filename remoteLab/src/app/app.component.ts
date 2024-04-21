import { Component } from '@angular/core';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { RouterOutlet } from '@angular/router';
import { EnParaleloComponent } from './en-paralelo/en-paralelo.component';
import { EnSerieComponent } from './en-serie/en-serie.component';
import { TimerComponent } from './timer/timer.component';
import { ToggleButtonComponent } from './toggle-button/toggle-button.component';

@Component({
  selector: 'app-root',
  standalone: true, 
  imports: [RouterOutlet, TimerComponent, ToggleButtonComponent, EnSerieComponent, EnParaleloComponent, MatProgressSpinnerModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'LabRemoto';
  tipoCircuito = "EnSerie";

  setTipoCircuito(tipo: string) {
    this.tipoCircuito = tipo;
  }
}
