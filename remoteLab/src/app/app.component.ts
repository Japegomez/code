import { Component } from '@angular/core';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { RouterOutlet } from '@angular/router';
import { EnParaleloComponent } from './components/en-paralelo/en-paralelo.component';
import { EnSerieComponent } from './components/en-serie/en-serie.component';
import { SerieYParaleloComponent } from './components/serie-yparalelo/serie-yparalelo.component';
import { TimerComponent } from './components/timer/timer.component';
import { ToggleButtonComponent } from './components/toggle-button/toggle-button.component';

@Component({
  selector: 'app-root',
  standalone: true, 
  imports: [RouterOutlet, TimerComponent, ToggleButtonComponent, EnSerieComponent, EnParaleloComponent, MatProgressSpinnerModule, SerieYParaleloComponent],
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
