<!--gcc-x64/comparison_table.cpp.txt-->
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">29.51</td>
    <td align="right">17.15</td>
    <td align="right">6.08</td>
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
    <td align="right">14.20</td>
    <td align="right">13.22</td>
    <td align="right">17.78</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.87</td>
    <td align="right">5.04</td>
    <td align="right">5.17</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">7.22</td>
    <td align="right">6.89</td>
    <td align="right">6.92</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">19.94</td>
    <td align="right">18.41</td>
    <td align="right">17.96</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">5.45</td>
    <td align="right">5.53</td>
    <td align="right">5.48</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.91</td>
    <td align="right">9.77</td>
    <td align="right">9.63</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">28.60</td>
    <td align="right">25.87</td>
    <td align="right">18.36</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">6.64</td>
    <td align="right">6.37</td>
    <td align="right">7.21</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">12.65</td>
    <td align="right">15.12</td>
    <td align="right">15.03</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">41.32</td>
    <td align="right">41.29</td>
    <td align="right">19.00</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">8.40</td>
    <td align="right">8.72</td>
    <td align="right">8.64</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">15.76</td>
    <td align="right">19.07</td>
    <td align="right">19.87</td>
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
    <td align="right">8.18</td>
    <td align="right">10.69</td>
    <td align="right">10.71</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.68</td>
    <td align="right">5.82</td>
    <td align="right">5.87</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">7.39</td>
    <td align="right">6.79</td>
    <td align="right">6.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5394</td>
    <td align="right">4.17</td>
    <td align="right">4.99</td>
    <td align="right">4.86</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">6.17</td>
    <td align="right">6.17</td>
    <td align="right">6.17</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">11.96</td>
    <td align="right">9.73</td>
    <td align="right">9.78</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1161</td>
    <td align="right">17.48</td>
    <td align="right">11.28</td>
    <td align="right">9.29</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">7.31</td>
    <td align="right">7.40</td>
    <td align="right">7.42</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">13.17</td>
    <td align="right">13.83</td>
    <td align="right">13.51</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0287</td>
    <td align="right">13.12</td>
    <td align="right">16.20</td>
    <td align="right">9.56</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">9.68</td>
    <td align="right">9.55</td>
    <td align="right">9.73</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">18.14</td>
    <td align="right">18.93</td>
    <td align="right">18.57</td>
  </tr>
</table>

<!--gcc-x64/comparison_table.cpp.txt-->

<!--clang-arm64/comparison_table.cpp.txt-->
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">39.76</td>
    <td align="right">19.04</td>
    <td align="right">14.14</td>
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
    <td align="right">16.49</td>
    <td align="right">14.71</td>
    <td align="right">28.09</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">5.16</td>
    <td align="right">5.91</td>
    <td align="right">4.12</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">4.88</td>
    <td align="right">6.04</td>
    <td align="right">6.28</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">41.27</td>
    <td align="right">32.18</td>
    <td align="right">28.28</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">9.40</td>
    <td align="right">8.00</td>
    <td align="right">7.41</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">14.57</td>
    <td align="right">16.26</td>
    <td align="right">14.93</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">77.71</td>
    <td align="right">56.96</td>
    <td align="right">26.71</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">14.84</td>
    <td align="right">15.73</td>
    <td align="right">14.50</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">25.49</td>
    <td align="right">14.12</td>
    <td align="right">15.02</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">104.35</td>
    <td align="right">94.36</td>
    <td align="right">37.77</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">20.05</td>
    <td align="right">15.41</td>
    <td align="right">15.95</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">31.79</td>
    <td align="right">24.12</td>
    <td align="right">24.94</td>
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
    <td align="right">6.26</td>
    <td align="right">5.82</td>
    <td align="right">7.97</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">4.50</td>
    <td align="right">3.83</td>
    <td align="right">5.10</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">5.47</td>
    <td align="right">6.52</td>
    <td align="right">5.50</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">7.11</td>
    <td align="right">8.17</td>
    <td align="right">8.06</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">8.15</td>
    <td align="right">8.25</td>
    <td align="right">8.63</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">10.18</td>
    <td align="right">12.35</td>
    <td align="right">11.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">15.44</td>
    <td align="right">14.49</td>
    <td align="right">10.84</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">11.21</td>
    <td align="right">10.31</td>
    <td align="right">9.49</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">16.01</td>
    <td align="right">15.53</td>
    <td align="right">13.99</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0276</td>
    <td align="right">15.58</td>
    <td align="right">20.65</td>
    <td align="right">10.39</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">10.91</td>
    <td align="right">9.05</td>
    <td align="right">9.35</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">23.68</td>
    <td align="right">16.30</td>
    <td align="right">16.62</td>
  </tr>
</table>

<!--clang-arm64/comparison_table.cpp.txt-->
