import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import { CountdownComponent, CountdownConfig, CountdownEvent } from 'ngx-countdown';

const KEY = 'time';
const DEFAULT = 4;

@Component({
  selector: 'app-timer',
  host: {
    '[class.card]': `true`,
    '[class.text-center]': `true`,
  },
  changeDetection: ChangeDetectionStrategy.OnPush,
  standalone: true,
  templateUrl: './timer.component.html',
  imports: [CountdownComponent],
})
export class TimerComponent implements OnInit {
  config: CountdownConfig = { leftTime: DEFAULT, notify: 0 };
  ngOnInit(): void {
    let value = +localStorage.getItem(KEY)!!;
    if (value <= 0) value = DEFAULT;
    this.config = { ...this.config, leftTime: value };
  }

  handleEvent(ev: CountdownEvent) {
    if (ev.action === 'notify') {
      // Save current value
      localStorage.setItem(KEY, `${ev.left / 1000}`);

      if ( ev.left === 0 ) {
        // Reset value
        console.log('Time is up!');
      }
    }
  }
}