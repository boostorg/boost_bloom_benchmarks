### GCC 14, x64
<!--gcc-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">25.97</td>
    <td align="right">4.30</td>
    <td align="right">3.46</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">10.84</td>
    <td align="right">10.70</td>
    <td align="right">16.56</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">4.04</td>
    <td align="right">4.21</td>
    <td align="right">4.29</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">6.01</td>
    <td align="right">5.75</td>
    <td align="right">5.75</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">17.58</td>
    <td align="right">15.28</td>
    <td align="right">17.40</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.84</td>
    <td align="right">4.84</td>
    <td align="right">4.83</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.01</td>
    <td align="right">8.85</td>
    <td align="right">8.86</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">20.29</td>
    <td align="right">18.66</td>
    <td align="right">16.73</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">5.41</td>
    <td align="right">5.32</td>
    <td align="right">5.47</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">10.18</td>
    <td align="right">13.77</td>
    <td align="right">13.72</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">27.18</td>
    <td align="right">23.39</td>
    <td align="right">16.73</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">6.20</td>
    <td align="right">6.17</td>
    <td align="right">5.92</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">12.10</td>
    <td align="right">15.77</td>
    <td align="right">15.78</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7421</td>
    <td align="right">8.04</td>
    <td align="right">10.63</td>
    <td align="right">10.57</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.84</td>
    <td align="right">5.02</td>
    <td align="right">5.02</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">6.17</td>
    <td align="right">5.78</td>
    <td align="right">5.75</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5384</td>
    <td align="right">3.71</td>
    <td align="right">4.75</td>
    <td align="right">4.74</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">5.44</td>
    <td align="right">5.60</td>
    <td align="right">5.56</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">11.70</td>
    <td align="right">9.07</td>
    <td align="right">9.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1163</td>
    <td align="right">17.17</td>
    <td align="right">10.48</td>
    <td align="right">8.29</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">6.24</td>
    <td align="right">6.28</td>
    <td align="right">6.26</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">11.28</td>
    <td align="right">11.70</td>
    <td align="right">11.72</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0286</td>
    <td align="right">9.06</td>
    <td align="right">10.61</td>
    <td align="right">6.09</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.65</td>
    <td align="right">6.65</td>
    <td align="right">6.65</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">13.39</td>
    <td align="right">14.67</td>
    <td align="right">14.69</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">30.32</td>
    <td align="right">19.46</td>
    <td align="right">6.48</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">12.98</td>
    <td align="right">12.10</td>
    <td align="right">17.25</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.50</td>
    <td align="right">4.66</td>
    <td align="right">4.78</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">6.70</td>
    <td align="right">6.49</td>
    <td align="right">6.51</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">18.51</td>
    <td align="right">16.78</td>
    <td align="right">17.54</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">5.15</td>
    <td align="right">5.28</td>
    <td align="right">5.11</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.56</td>
    <td align="right">9.31</td>
    <td align="right">9.29</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">30.76</td>
    <td align="right">22.47</td>
    <td align="right">17.16</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">7.26</td>
    <td align="right">5.90</td>
    <td align="right">6.03</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">11.53</td>
    <td align="right">14.86</td>
    <td align="right">14.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">35.34</td>
    <td align="right">33.02</td>
    <td align="right">17.72</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">8.07</td>
    <td align="right">7.52</td>
    <td align="right">7.74</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">14.59</td>
    <td align="right">21.44</td>
    <td align="right">19.29</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7269</td>
    <td align="right">8.20</td>
    <td align="right">10.78</td>
    <td align="right">10.76</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.47</td>
    <td align="right">5.59</td>
    <td align="right">5.59</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">6.87</td>
    <td align="right">6.30</td>
    <td align="right">6.34</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5394</td>
    <td align="right">4.02</td>
    <td align="right">5.07</td>
    <td align="right">5.10</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">5.85</td>
    <td align="right">5.86</td>
    <td align="right">5.86</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">11.71</td>
    <td align="right">10.00</td>
    <td align="right">10.05</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1161</td>
    <td align="right">17.35</td>
    <td align="right">11.70</td>
    <td align="right">9.39</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">7.68</td>
    <td align="right">9.70</td>
    <td align="right">8.63</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">13.50</td>
    <td align="right">13.57</td>
    <td align="right">13.74</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0287</td>
    <td align="right">16.86</td>
    <td align="right">14.80</td>
    <td align="right">7.04</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">11.52</td>
    <td align="right">13.44</td>
    <td align="right">8.76</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">18.52</td>
    <td align="right">16.42</td>
    <td align="right">17.25</td>
  </tr>
</table>

<!--gcc-x64/comparison_table.cpp.txt-->

### Clang 18, X64
<!--clang-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">31.55</td>
    <td align="right">7.62</td>
    <td align="right">4.29</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">8.80</td>
    <td align="right">8.42</td>
    <td align="right">16.18</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.20</td>
    <td align="right">3.77</td>
    <td align="right">3.80</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">5.11</td>
    <td align="right">5.30</td>
    <td align="right">5.44</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">12.67</td>
    <td align="right">12.60</td>
    <td align="right">16.72</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">3.66</td>
    <td align="right">4.46</td>
    <td align="right">4.38</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.84</td>
    <td align="right">8.16</td>
    <td align="right">8.07</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">16.54</td>
    <td align="right">15.16</td>
    <td align="right">16.30</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">4.19</td>
    <td align="right">4.87</td>
    <td align="right">4.92</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">10.07</td>
    <td align="right">14.54</td>
    <td align="right">14.08</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">19.37</td>
    <td align="right">18.70</td>
    <td align="right">15.67</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">4.88</td>
    <td align="right">5.54</td>
    <td align="right">5.68</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">14.94</td>
    <td align="right">14.30</td>
    <td align="right">15.14</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7421</td>
    <td align="right">3.41</td>
    <td align="right">4.08</td>
    <td align="right">4.01</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">3.80</td>
    <td align="right">4.45</td>
    <td align="right">4.42</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">4.87</td>
    <td align="right">5.31</td>
    <td align="right">5.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5384</td>
    <td align="right">2.76</td>
    <td align="right">3.74</td>
    <td align="right">3.61</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">4.36</td>
    <td align="right">5.29</td>
    <td align="right">5.19</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">7.23</td>
    <td align="right">8.36</td>
    <td align="right">8.47</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1163</td>
    <td align="right">10.54</td>
    <td align="right">6.10</td>
    <td align="right">4.63</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">4.98</td>
    <td align="right">5.96</td>
    <td align="right">5.92</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">15.89</td>
    <td align="right">13.98</td>
    <td align="right">12.44</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0286</td>
    <td align="right">5.90</td>
    <td align="right">6.61</td>
    <td align="right">4.31</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">5.54</td>
    <td align="right">6.32</td>
    <td align="right">6.24</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">17.52</td>
    <td align="right">14.01</td>
    <td align="right">13.84</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">47.79</td>
    <td align="right">32.53</td>
    <td align="right">18.30</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">11.88</td>
    <td align="right">11.44</td>
    <td align="right">18.30</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.72</td>
    <td align="right">5.11</td>
    <td align="right">5.18</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">7.51</td>
    <td align="right">7.67</td>
    <td align="right">7.66</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">18.43</td>
    <td align="right">20.96</td>
    <td align="right">18.62</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">5.80</td>
    <td align="right">9.36</td>
    <td align="right">9.02</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">12.04</td>
    <td align="right">12.53</td>
    <td align="right">12.24</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">30.37</td>
    <td align="right">32.52</td>
    <td align="right">20.03</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">13.01</td>
    <td align="right">9.41</td>
    <td align="right">7.12</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">16.10</td>
    <td align="right">18.94</td>
    <td align="right">20.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">131.77</td>
    <td align="right">146.33</td>
    <td align="right">37.59</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">12.04</td>
    <td align="right">25.35</td>
    <td align="right">32.66</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">66.12</td>
    <td align="right">67.22</td>
    <td align="right">65.86</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7269</td>
    <td align="right">6.15</td>
    <td align="right">6.72</td>
    <td align="right">6.20</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">6.25</td>
    <td align="right">5.77</td>
    <td align="right">5.49</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">6.97</td>
    <td align="right">9.12</td>
    <td align="right">8.40</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5394</td>
    <td align="right">12.14</td>
    <td align="right">16.22</td>
    <td align="right">19.89</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">12.08</td>
    <td align="right">6.95</td>
    <td align="right">6.91</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">11.17</td>
    <td align="right">27.94</td>
    <td align="right">35.19</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1161</td>
    <td align="right">34.38</td>
    <td align="right">40.30</td>
    <td align="right">33.44</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">30.40</td>
    <td align="right">34.63</td>
    <td align="right">34.67</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">66.82</td>
    <td align="right">77.22</td>
    <td align="right">67.53</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0287</td>
    <td align="right">41.97</td>
    <td align="right">36.66</td>
    <td align="right">19.60</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">12.64</td>
    <td align="right">17.18</td>
    <td align="right">18.23</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">28.97</td>
    <td align="right">31.54</td>
    <td align="right">31.14</td>
  </tr>
</table>

<!--clang-x64/comparison_table.cpp.txt-->

### Clang 15, ARM64
<!--clang-arm64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">22.23</td>
    <td align="right">7.79</td>
    <td align="right">3.58</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">9.53</td>
    <td align="right">5.70</td>
    <td align="right">12.43</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">1.50</td>
    <td align="right">1.64</td>
    <td align="right">1.63</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">3.37</td>
    <td align="right">1.84</td>
    <td align="right">1.86</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">11.65</td>
    <td align="right">7.57</td>
    <td align="right">15.79</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">1.90</td>
    <td align="right">3.16</td>
    <td align="right">1.94</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.69</td>
    <td align="right">2.96</td>
    <td align="right">4.10</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">20.72</td>
    <td align="right">11.63</td>
    <td align="right">12.53</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">3.36</td>
    <td align="right">2.33</td>
    <td align="right">2.26</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">5.90</td>
    <td align="right">4.78</td>
    <td align="right">4.28</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">24.29</td>
    <td align="right">14.39</td>
    <td align="right">17.66</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">1.99</td>
    <td align="right">2.01</td>
    <td align="right">2.29</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">5.19</td>
    <td align="right">4.03</td>
    <td align="right">4.18</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.06</td>
    <td align="right">3.45</td>
    <td align="right">3.17</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">1.95</td>
    <td align="right">2.39</td>
    <td align="right">2.06</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">4.12</td>
    <td align="right">2.63</td>
    <td align="right">2.21</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.23</td>
    <td align="right">1.91</td>
    <td align="right">1.72</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">1.94</td>
    <td align="right">1.64</td>
    <td align="right">1.61</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.34</td>
    <td align="right">2.56</td>
    <td align="right">2.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">3.34</td>
    <td align="right">3.05</td>
    <td align="right">2.53</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">1.98</td>
    <td align="right">1.67</td>
    <td align="right">1.92</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.63</td>
    <td align="right">3.38</td>
    <td align="right">3.51</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0304</td>
    <td align="right">4.31</td>
    <td align="right">3.70</td>
    <td align="right">2.40</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">4.59</td>
    <td align="right">2.77</td>
    <td align="right">2.37</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">6.21</td>
    <td align="right">6.04</td>
    <td align="right">5.74</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">31.60</td>
    <td align="right">16.14</td>
    <td align="right">10.03</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">13.26</td>
    <td align="right">11.73</td>
    <td align="right">22.83</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">3.42</td>
    <td align="right">3.96</td>
    <td align="right">4.80</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">4.63</td>
    <td align="right">6.38</td>
    <td align="right">5.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">29.62</td>
    <td align="right">26.70</td>
    <td align="right">25.55</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">7.88</td>
    <td align="right">7.95</td>
    <td align="right">8.59</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">10.38</td>
    <td align="right">9.61</td>
    <td align="right">10.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">54.80</td>
    <td align="right">46.38</td>
    <td align="right">25.15</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">11.22</td>
    <td align="right">8.52</td>
    <td align="right">9.54</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">17.64</td>
    <td align="right">14.84</td>
    <td align="right">14.02</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">79.65</td>
    <td align="right">60.67</td>
    <td align="right">29.29</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">12.21</td>
    <td align="right">12.65</td>
    <td align="right">12.17</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">21.86</td>
    <td align="right">18.31</td>
    <td align="right">17.55</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.06</td>
    <td align="right">4.95</td>
    <td align="right">5.68</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">2.91</td>
    <td align="right">3.30</td>
    <td align="right">3.62</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">4.36</td>
    <td align="right">4.94</td>
    <td align="right">4.81</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">6.62</td>
    <td align="right">8.59</td>
    <td align="right">6.83</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">3.17</td>
    <td align="right">5.34</td>
    <td align="right">4.73</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">6.57</td>
    <td align="right">10.70</td>
    <td align="right">10.63</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">13.32</td>
    <td align="right">13.07</td>
    <td align="right">9.79</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">11.43</td>
    <td align="right">9.41</td>
    <td align="right">10.91</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">19.88</td>
    <td align="right">16.83</td>
    <td align="right">17.51</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0276</td>
    <td align="right">14.35</td>
    <td align="right">15.04</td>
    <td align="right">10.64</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">11.49</td>
    <td align="right">10.17</td>
    <td align="right">9.97</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">23.52</td>
    <td align="right">20.32</td>
    <td align="right">21.17</td>
  </tr>
</table>

<!--clang-arm64/comparison_table.cpp.txt-->

### VS 2022, x64
<!--vs-x64/comparison_table.cpp.txt-->
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">36.57</td>
    <td align="right">5.82</td>
    <td align="right">3.84</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">11.96</td>
    <td align="right">12.43</td>
    <td align="right">16.90</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">5.82</td>
    <td align="right">4.44</td>
    <td align="right">4.41</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">7.85</td>
    <td align="right">6.00</td>
    <td align="right">6.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">18.25</td>
    <td align="right">17.57</td>
    <td align="right">17.49</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">6.95</td>
    <td align="right">5.01</td>
    <td align="right">5.32</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">11.58</td>
    <td align="right">8.40</td>
    <td align="right">8.43</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">23.39</td>
    <td align="right">21.14</td>
    <td align="right">16.52</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">8.61</td>
    <td align="right">5.71</td>
    <td align="right">5.70</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">15.53</td>
    <td align="right">13.04</td>
    <td align="right">13.45</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">30.89</td>
    <td align="right">26.46</td>
    <td align="right">17.00</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">9.85</td>
    <td align="right">6.29</td>
    <td align="right">6.33</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">17.97</td>
    <td align="right">15.86</td>
    <td align="right">16.03</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7421</td>
    <td align="right">7.68</td>
    <td align="right">10.67</td>
    <td align="right">10.62</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">6.93</td>
    <td align="right">5.28</td>
    <td align="right">5.18</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">14.02</td>
    <td align="right">5.64</td>
    <td align="right">5.89</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5384</td>
    <td align="right">3.60</td>
    <td align="right">6.07</td>
    <td align="right">5.37</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">7.99</td>
    <td align="right">5.90</td>
    <td align="right">5.87</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">25.94</td>
    <td align="right">8.31</td>
    <td align="right">8.28</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1163</td>
    <td align="right">9.00</td>
    <td align="right">10.16</td>
    <td align="right">7.19</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">9.32</td>
    <td align="right">6.46</td>
    <td align="right">6.63</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">16.09</td>
    <td align="right">11.53</td>
    <td align="right">11.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0286</td>
    <td align="right">7.01</td>
    <td align="right">11.38</td>
    <td align="right">7.39</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">10.27</td>
    <td align="right">7.25</td>
    <td align="right">7.32</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">19.18</td>
    <td align="right">16.39</td>
    <td align="right">16.33</td>
  </tr>
</table>
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">42.64</td>
    <td align="right">21.90</td>
    <td align="right">7.25</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">14.36</td>
    <td align="right">12.93</td>
    <td align="right">17.58</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">6.99</td>
    <td align="right">4.75</td>
    <td align="right">4.67</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">9.35</td>
    <td align="right">6.66</td>
    <td align="right">6.61</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">21.89</td>
    <td align="right">18.62</td>
    <td align="right">18.28</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">8.46</td>
    <td align="right">5.37</td>
    <td align="right">5.41</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">13.66</td>
    <td align="right">9.62</td>
    <td align="right">9.59</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">33.87</td>
    <td align="right">25.14</td>
    <td align="right">17.51</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">10.46</td>
    <td align="right">6.42</td>
    <td align="right">6.30</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">17.81</td>
    <td align="right">15.55</td>
    <td align="right">15.44</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">54.98</td>
    <td align="right">52.68</td>
    <td align="right">19.69</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">12.86</td>
    <td align="right">8.73</td>
    <td align="right">9.28</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">23.16</td>
    <td align="right">21.25</td>
    <td align="right">20.87</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7269</td>
    <td align="right">7.80</td>
    <td align="right">10.74</td>
    <td align="right">10.68</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">7.88</td>
    <td align="right">5.51</td>
    <td align="right">5.59</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">14.14</td>
    <td align="right">6.05</td>
    <td align="right">6.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5394</td>
    <td align="right">3.97</td>
    <td align="right">6.50</td>
    <td align="right">5.81</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">9.18</td>
    <td align="right">6.29</td>
    <td align="right">6.29</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">26.10</td>
    <td align="right">8.97</td>
    <td align="right">8.99</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1161</td>
    <td align="right">9.35</td>
    <td align="right">10.63</td>
    <td align="right">7.77</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">10.34</td>
    <td align="right">7.04</td>
    <td align="right">7.00</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">17.10</td>
    <td align="right">12.49</td>
    <td align="right">12.45</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0287</td>
    <td align="right">10.34</td>
    <td align="right">15.59</td>
    <td align="right">11.79</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">12.32</td>
    <td align="right">9.43</td>
    <td align="right">8.88</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">23.85</td>
    <td align="right">20.72</td>
    <td align="right">20.83</td>
  </tr>
</table>

<!--vs-x64/comparison_table.cpp.txt-->
