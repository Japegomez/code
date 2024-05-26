import { ChangeDetectionStrategy, Component, Input, OnInit, ViewChild } from '@angular/core';
import { CountdownComponent, CountdownConfig, CountdownEvent } from 'ngx-countdown';

@Component({
  selector: 'app-timer',
  host: {
    '[class.card]': `true`,
    '[class.text-center]': `true`,
  },
  changeDetection: ChangeDetectionStrategy.Default,
  standalone: true,
  templateUrl: './timer.component.html',
  imports: [CountdownComponent],
})
export class TimerComponent implements OnInit {
  @Input() timeLeft = 0;
  config: CountdownConfig = { leftTime: -1, notify: 0 };
  @ViewChild('countdown') counter!: CountdownComponent;

  ngOnInit(): void {
    this.config = { ...this.config, leftTime: this.timeLeft };
  }

  ngOnChanges() {
    if (this.counter) {
      this.config.leftTime = this.timeLeft;
      this.counter.config = this.config;
      this.counter?.restart();
    }
  }

  handleEvent(ev: CountdownEvent) {
    if (ev.action === 'notify' && ev.left === 0 && this.counter) {
      alert("Se ha acabado el tiempo"); // muestra por pantalla
    }
  }
}