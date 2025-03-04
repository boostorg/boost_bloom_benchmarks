# Experimental results for [candidate Boost Bloom Library](https://github.com/joaquintides/bloom)

The tables show the false positive rate (FPR) and execution times in nanoseconds per operation 
for six different configurations of `boost::bloom::filter<int, ...>`
where `N` elements have been inserted. Filters are constructed with a capacity
`c*N` (bits), so `c` is the number of bits used per element. For each combination of `c` and
a given filter configuration, we have selected the optimum value of `K` (that yielding the minimum FPR).
Standard release-mode settings are used; 
AVX2 is indicated for Visual Studio builds (`/arch:AVX2`) and 64-bit GCC/Clang builds (`-mavx2`),
which causes `fast_multiblock32` to use its AVX2 variant.

For reference, we provide also insertion, successful lookup and unsuccessful lookup times
for a `boost::unordered_flat_set<int>` with the same number of elements `N`.

## Results

* [GCC 14, x64](#gcc-14-x64)
* [Clang 18, x64](#clang-18-x64)
* [Clang 15, ARM64](#clang-15-arm64)
* [VS 2022, x64](#vs-2022-x64)
* [GCC 14, x86](#gcc-14-x86)
* [Clang 18, x86](#clang-18-x86)
* [VS 2022, x86](#vs-2022-x86)

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
    <td align="right">28.59</td>
    <td align="right">6.00</td>
    <td align="right">5.21</td>
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
    <td align="right">11.26</td>
    <td align="right">10.90</td>
    <td align="right">16.73</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">4.13</td>
    <td align="right">4.46</td>
    <td align="right">4.44</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">5.18</td>
    <td align="right">5.80</td>
    <td align="right">5.78</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">17.05</td>
    <td align="right">15.60</td>
    <td align="right">17.53</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.90</td>
    <td align="right">5.02</td>
    <td align="right">5.00</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.02</td>
    <td align="right">8.85</td>
    <td align="right">8.90</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">20.18</td>
    <td align="right">18.85</td>
    <td align="right">16.50</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">5.48</td>
    <td align="right">5.40</td>
    <td align="right">5.54</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">9.43</td>
    <td align="right">13.89</td>
    <td align="right">13.90</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">27.89</td>
    <td align="right">23.18</td>
    <td align="right">16.90</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">6.58</td>
    <td align="right">5.98</td>
    <td align="right">5.95</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">11.68</td>
    <td align="right">15.81</td>
    <td align="right">15.74</td>
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
    <td align="right">2.97</td>
    <td align="right">3.28</td>
    <td align="right">3.37</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.89</td>
    <td align="right">5.09</td>
    <td align="right">5.09</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">5.57</td>
    <td align="right">6.72</td>
    <td align="right">6.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.51</td>
    <td align="right">3.18</td>
    <td align="right">3.15</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">5.43</td>
    <td align="right">5.50</td>
    <td align="right">5.55</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.17</td>
    <td align="right">10.06</td>
    <td align="right">10.09</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">5.74</td>
    <td align="right">5.84</td>
    <td align="right">3.95</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">6.26</td>
    <td align="right">6.36</td>
    <td align="right">6.32</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">16.69</td>
    <td align="right">14.14</td>
    <td align="right">14.16</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0304</td>
    <td align="right">5.70</td>
    <td align="right">5.75</td>
    <td align="right">3.93</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.72</td>
    <td align="right">6.59</td>
    <td align="right">6.59</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">11.99</td>
    <td align="right">17.48</td>
    <td align="right">17.43</td>
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
    <td align="right">32.44</td>
    <td align="right">19.73</td>
    <td align="right">6.97</td>
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
    <td align="right">13.27</td>
    <td align="right">12.52</td>
    <td align="right">17.43</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.83</td>
    <td align="right">5.13</td>
    <td align="right">5.16</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">6.23</td>
    <td align="right">6.76</td>
    <td align="right">6.77</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">19.13</td>
    <td align="right">17.95</td>
    <td align="right">17.82</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">5.26</td>
    <td align="right">5.41</td>
    <td align="right">5.41</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">8.92</td>
    <td align="right">12.08</td>
    <td align="right">10.86</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">28.88</td>
    <td align="right">27.02</td>
    <td align="right">18.22</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">7.63</td>
    <td align="right">7.43</td>
    <td align="right">8.00</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">11.70</td>
    <td align="right">15.92</td>
    <td align="right">15.95</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">68.82</td>
    <td align="right">56.40</td>
    <td align="right">20.36</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">13.57</td>
    <td align="right">12.67</td>
    <td align="right">13.48</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">19.09</td>
    <td align="right">22.27</td>
    <td align="right">23.50</td>
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
    <td align="right">3.51</td>
    <td align="right">3.97</td>
    <td align="right">4.00</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.66</td>
    <td align="right">5.86</td>
    <td align="right">5.84</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">6.40</td>
    <td align="right">7.79</td>
    <td align="right">8.02</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">3.14</td>
    <td align="right">4.22</td>
    <td align="right">3.73</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">5.97</td>
    <td align="right">6.59</td>
    <td align="right">6.70</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">13.05</td>
    <td align="right">16.09</td>
    <td align="right">14.44</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">12.12</td>
    <td align="right">10.02</td>
    <td align="right">6.13</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">9.22</td>
    <td align="right">9.06</td>
    <td align="right">9.87</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">21.83</td>
    <td align="right">17.47</td>
    <td align="right">20.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0276</td>
    <td align="right">19.50</td>
    <td align="right">21.11</td>
    <td align="right">12.89</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">21.14</td>
    <td align="right">17.08</td>
    <td align="right">15.69</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">21.77</td>
    <td align="right">33.49</td>
    <td align="right">31.51</td>
  </tr>
</table>

<!--gcc-x64/comparison_table.cpp.txt-->

### Clang 18, x64
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
    <td align="right">26.90</td>
    <td align="right">4.25</td>
    <td align="right">3.49</td>
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
    <td align="right">9.43</td>
    <td align="right">9.05</td>
    <td align="right">15.45</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.32</td>
    <td align="right">4.04</td>
    <td align="right">3.95</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">3.11</td>
    <td align="right">3.60</td>
    <td align="right">3.63</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">14.01</td>
    <td align="right">13.66</td>
    <td align="right">16.54</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">3.90</td>
    <td align="right">4.56</td>
    <td align="right">4.73</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.70</td>
    <td align="right">3.36</td>
    <td align="right">3.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">17.42</td>
    <td align="right">16.57</td>
    <td align="right">15.81</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">4.36</td>
    <td align="right">5.07</td>
    <td align="right">5.09</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">5.64</td>
    <td align="right">6.45</td>
    <td align="right">6.22</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">20.29</td>
    <td align="right">21.05</td>
    <td align="right">16.02</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">4.86</td>
    <td align="right">5.88</td>
    <td align="right">5.86</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">5.89</td>
    <td align="right">6.91</td>
    <td align="right">6.89</td>
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
    <td align="right">2.59</td>
    <td align="right">2.53</td>
    <td align="right">2.53</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">3.88</td>
    <td align="right">4.69</td>
    <td align="right">4.57</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">3.17</td>
    <td align="right">3.52</td>
    <td align="right">3.51</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.15</td>
    <td align="right">2.27</td>
    <td align="right">2.27</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">4.52</td>
    <td align="right">5.31</td>
    <td align="right">5.29</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.77</td>
    <td align="right">3.79</td>
    <td align="right">3.75</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.16</td>
    <td align="right">4.42</td>
    <td align="right">3.20</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">4.96</td>
    <td align="right">6.00</td>
    <td align="right">6.20</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">5.87</td>
    <td align="right">6.13</td>
    <td align="right">6.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0304</td>
    <td align="right">4.14</td>
    <td align="right">4.37</td>
    <td align="right">3.18</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">2.87</td>
    <td align="right">3.34</td>
    <td align="right">3.32</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">6.33</td>
    <td align="right">7.08</td>
    <td align="right">7.27</td>
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
    <td align="right">33.16</td>
    <td align="right">17.06</td>
    <td align="right">7.04</td>
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
    <td align="right">11.14</td>
    <td align="right">10.79</td>
    <td align="right">16.41</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">3.91</td>
    <td align="right">4.76</td>
    <td align="right">4.48</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">3.69</td>
    <td align="right">4.35</td>
    <td align="right">4.35</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">19.37</td>
    <td align="right">17.35</td>
    <td align="right">17.32</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">5.00</td>
    <td align="right">5.87</td>
    <td align="right">5.70</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.56</td>
    <td align="right">4.52</td>
    <td align="right">4.10</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">27.96</td>
    <td align="right">28.43</td>
    <td align="right">20.45</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">9.90</td>
    <td align="right">9.33</td>
    <td align="right">11.14</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">8.18</td>
    <td align="right">9.02</td>
    <td align="right">8.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">53.09</td>
    <td align="right">55.83</td>
    <td align="right">23.28</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">12.81</td>
    <td align="right">15.55</td>
    <td align="right">12.51</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">10.33</td>
    <td align="right">12.90</td>
    <td align="right">14.41</td>
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
    <td align="right">3.09</td>
    <td align="right">3.09</td>
    <td align="right">3.12</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">4.62</td>
    <td align="right">5.37</td>
    <td align="right">5.26</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.77</td>
    <td align="right">4.23</td>
    <td align="right">4.21</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.67</td>
    <td align="right">3.06</td>
    <td align="right">2.93</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">5.81</td>
    <td align="right">6.21</td>
    <td align="right">6.36</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.78</td>
    <td align="right">4.75</td>
    <td align="right">4.68</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">7.92</td>
    <td align="right">6.67</td>
    <td align="right">4.88</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">7.52</td>
    <td align="right">10.47</td>
    <td align="right">11.39</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">8.01</td>
    <td align="right">9.36</td>
    <td align="right">10.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0276</td>
    <td align="right">13.13</td>
    <td align="right">15.63</td>
    <td align="right">11.42</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">8.12</td>
    <td align="right">8.06</td>
    <td align="right">10.07</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">11.72</td>
    <td align="right">14.15</td>
    <td align="right">14.89</td>
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
    <td align="right">26.05</td>
    <td align="right">6.08</td>
    <td align="right">3.80</td>
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
    <td align="right">10.39</td>
    <td align="right">8.41</td>
    <td align="right">13.70</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">1.66</td>
    <td align="right">2.00</td>
    <td align="right">1.70</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.67</td>
    <td align="right">2.81</td>
    <td align="right">1.87</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">14.54</td>
    <td align="right">9.19</td>
    <td align="right">15.24</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">1.56</td>
    <td align="right">2.03</td>
    <td align="right">1.96</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.97</td>
    <td align="right">2.34</td>
    <td align="right">2.87</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">18.06</td>
    <td align="right">11.34</td>
    <td align="right">16.51</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">1.93</td>
    <td align="right">2.20</td>
    <td align="right">2.15</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">6.31</td>
    <td align="right">4.75</td>
    <td align="right">3.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">25.53</td>
    <td align="right">13.86</td>
    <td align="right">14.87</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">3.26</td>
    <td align="right">2.60</td>
    <td align="right">2.79</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">6.97</td>
    <td align="right">7.66</td>
    <td align="right">5.59</td>
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
    <td align="right">2.94</td>
    <td align="right">3.15</td>
    <td align="right">2.54</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">3.60</td>
    <td align="right">2.14</td>
    <td align="right">2.87</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">3.10</td>
    <td align="right">3.33</td>
    <td align="right">2.90</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.69</td>
    <td align="right">2.93</td>
    <td align="right">3.08</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">3.19</td>
    <td align="right">5.40</td>
    <td align="right">3.51</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.74</td>
    <td align="right">3.97</td>
    <td align="right">3.02</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">7.76</td>
    <td align="right">4.71</td>
    <td align="right">2.62</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">2.62</td>
    <td align="right">2.71</td>
    <td align="right">2.37</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">10.16</td>
    <td align="right">8.02</td>
    <td align="right">4.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0304</td>
    <td align="right">4.13</td>
    <td align="right">3.89</td>
    <td align="right">3.15</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">5.48</td>
    <td align="right">2.54</td>
    <td align="right">2.29</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">7.89</td>
    <td align="right">7.10</td>
    <td align="right">5.82</td>
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
    <td align="right">38.06</td>
    <td align="right">19.47</td>
    <td align="right">11.30</td>
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
    <td align="right">13.03</td>
    <td align="right">12.14</td>
    <td align="right">26.49</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">7.13</td>
    <td align="right">5.44</td>
    <td align="right">8.80</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">7.85</td>
    <td align="right">7.85</td>
    <td align="right">7.33</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">53.74</td>
    <td align="right">40.81</td>
    <td align="right">33.47</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">12.92</td>
    <td align="right">10.09</td>
    <td align="right">8.82</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">13.06</td>
    <td align="right">15.07</td>
    <td align="right">14.39</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">76.57</td>
    <td align="right">60.59</td>
    <td align="right">33.50</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">16.14</td>
    <td align="right">14.53</td>
    <td align="right">15.14</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">26.43</td>
    <td align="right">21.64</td>
    <td align="right">20.95</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">102.78</td>
    <td align="right">65.70</td>
    <td align="right">30.70</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">18.65</td>
    <td align="right">16.30</td>
    <td align="right">12.28</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">32.10</td>
    <td align="right">23.93</td>
    <td align="right">23.70</td>
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
    <td align="right">5.72</td>
    <td align="right">7.42</td>
    <td align="right">9.38</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">4.04</td>
    <td align="right">4.78</td>
    <td align="right">7.52</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">7.91</td>
    <td align="right">9.24</td>
    <td align="right">9.00</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">9.76</td>
    <td align="right">12.15</td>
    <td align="right">11.27</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">11.79</td>
    <td align="right">10.71</td>
    <td align="right">12.33</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">15.98</td>
    <td align="right">16.96</td>
    <td align="right">15.57</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">19.46</td>
    <td align="right">14.62</td>
    <td align="right">12.26</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">11.53</td>
    <td align="right">10.52</td>
    <td align="right">9.17</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">18.79</td>
    <td align="right">16.10</td>
    <td align="right">18.18</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0276</td>
    <td align="right">14.54</td>
    <td align="right">16.33</td>
    <td align="right">9.13</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">11.20</td>
    <td align="right">8.94</td>
    <td align="right">9.06</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">25.80</td>
    <td align="right">23.71</td>
    <td align="right">19.69</td>
  </tr>
</table>

<!--clang-arm64/comparison_table.cpp.txt-->

### VS 2022, x64
<!--vs-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">36.71</td>
    <td align="right">5.87</td>
    <td align="right">4.23</td>
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
    <td align="right">12.16</td>
    <td align="right">12.68</td>
    <td align="right">17.26</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">5.86</td>
    <td align="right">4.35</td>
    <td align="right">4.30</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">7.97</td>
    <td align="right">5.72</td>
    <td align="right">5.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">18.73</td>
    <td align="right">18.06</td>
    <td align="right">17.76</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">7.02</td>
    <td align="right">5.03</td>
    <td align="right">4.86</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">11.72</td>
    <td align="right">8.68</td>
    <td align="right">8.57</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">23.99</td>
    <td align="right">21.78</td>
    <td align="right">16.87</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">8.61</td>
    <td align="right">5.61</td>
    <td align="right">5.36</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">15.65</td>
    <td align="right">11.29</td>
    <td align="right">11.13</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">31.45</td>
    <td align="right">27.59</td>
    <td align="right">17.71</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">10.03</td>
    <td align="right">6.05</td>
    <td align="right">6.11</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">18.04</td>
    <td align="right">14.74</td>
    <td align="right">14.91</td>
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
    <td align="right">3.41</td>
    <td align="right">3.91</td>
    <td align="right">4.01</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">7.00</td>
    <td align="right">5.27</td>
    <td align="right">5.29</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">11.74</td>
    <td align="right">5.64</td>
    <td align="right">5.66</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.98</td>
    <td align="right">4.90</td>
    <td align="right">4.10</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">8.01</td>
    <td align="right">6.06</td>
    <td align="right">5.93</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">15.35</td>
    <td align="right">8.74</td>
    <td align="right">7.89</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.92</td>
    <td align="right">7.04</td>
    <td align="right">5.35</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">9.33</td>
    <td align="right">6.55</td>
    <td align="right">6.56</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">15.97</td>
    <td align="right">10.38</td>
    <td align="right">10.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0304</td>
    <td align="right">5.00</td>
    <td align="right">7.08</td>
    <td align="right">5.28</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">10.43</td>
    <td align="right">7.42</td>
    <td align="right">7.56</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">18.88</td>
    <td align="right">12.98</td>
    <td align="right">13.65</td>
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
    <td align="right">45.25</td>
    <td align="right">23.35</td>
    <td align="right">9.73</td>
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
    <td align="right">14.69</td>
    <td align="right">14.58</td>
    <td align="right">17.97</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">7.10</td>
    <td align="right">4.48</td>
    <td align="right">4.48</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">9.35</td>
    <td align="right">6.49</td>
    <td align="right">6.71</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">27.17</td>
    <td align="right">26.06</td>
    <td align="right">19.59</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">8.79</td>
    <td align="right">5.20</td>
    <td align="right">5.21</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">14.76</td>
    <td align="right">11.24</td>
    <td align="right">11.49</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">34.38</td>
    <td align="right">32.06</td>
    <td align="right">19.27</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">12.30</td>
    <td align="right">7.89</td>
    <td align="right">7.67</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">21.19</td>
    <td align="right">16.19</td>
    <td align="right">17.35</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">70.20</td>
    <td align="right">48.01</td>
    <td align="right">22.26</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">20.23</td>
    <td align="right">18.24</td>
    <td align="right">16.92</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">31.78</td>
    <td align="right">31.05</td>
    <td align="right">23.68</td>
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
    <td align="right">3.69</td>
    <td align="right">4.22</td>
    <td align="right">4.27</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">7.95</td>
    <td align="right">5.58</td>
    <td align="right">5.59</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">9.51</td>
    <td align="right">6.25</td>
    <td align="right">6.28</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">3.30</td>
    <td align="right">5.35</td>
    <td align="right">4.45</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">9.40</td>
    <td align="right">6.57</td>
    <td align="right">6.42</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">15.60</td>
    <td align="right">9.34</td>
    <td align="right">8.70</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">6.39</td>
    <td align="right">9.17</td>
    <td align="right">8.65</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">14.96</td>
    <td align="right">18.74</td>
    <td align="right">11.08</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">20.81</td>
    <td align="right">14.67</td>
    <td align="right">15.95</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0276</td>
    <td align="right">13.69</td>
    <td align="right">17.54</td>
    <td align="right">15.28</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">20.70</td>
    <td align="right">24.99</td>
    <td align="right">23.78</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">36.47</td>
    <td align="right">27.49</td>
    <td align="right">27.03</td>
  </tr>
</table>

<!--vs-x64/comparison_table.cpp.txt-->

### GCC 14, x86
<!--gcc-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">60.14</td>
    <td align="right">31.64</td>
    <td align="right">16.88</td>
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
    <td align="right">2.1546</td>
    <td align="right">27.11</td>
    <td align="right">41.20</td>
    <td align="right">35.91</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">12.38</td>
    <td align="right">15.91</td>
    <td align="right">15.91</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">16.22</td>
    <td align="right">20.13</td>
    <td align="right">20.16</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">36.81</td>
    <td align="right">63.19</td>
    <td align="right">39.03</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">17.29</td>
    <td align="right">19.45</td>
    <td align="right">19.23</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">20.98</td>
    <td align="right">26.74</td>
    <td align="right">26.80</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">44.44</td>
    <td align="right">77.32</td>
    <td align="right">38.14</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.55</td>
    <td align="right">18.52</td>
    <td align="right">18.42</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.02</td>
    <td align="right">33.08</td>
    <td align="right">32.99</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">52.25</td>
    <td align="right">89.41</td>
    <td align="right">35.33</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">17.26</td>
    <td align="right">18.57</td>
    <td align="right">18.57</td>
    <td align="center">14</td>
    <td align="right">0.0149</td>
    <td align="right">33.83</td>
    <td align="right">35.90</td>
    <td align="right">35.87</td>
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
    <td align="right">2.7635</td>
    <td align="right">10.54</td>
    <td align="right">13.59</td>
    <td align="right">13.56</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">16.08</td>
    <td align="right">19.75</td>
    <td align="right">19.69</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.50</td>
    <td align="right">22.20</td>
    <td align="right">22.15</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">12.81</td>
    <td align="right">16.48</td>
    <td align="right">15.88</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">16.09</td>
    <td align="right">18.69</td>
    <td align="right">18.58</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.58</td>
    <td align="right">28.92</td>
    <td align="right">28.98</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">14.49</td>
    <td align="right">19.49</td>
    <td align="right">19.47</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">18.06</td>
    <td align="right">18.57</td>
    <td align="right">18.29</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">64.56</td>
    <td align="right">45.76</td>
    <td align="right">45.66</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0297</td>
    <td align="right">22.95</td>
    <td align="right">24.04</td>
    <td align="right">24.04</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">18.17</td>
    <td align="right">19.59</td>
    <td align="right">19.59</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">75.98</td>
    <td align="right">53.92</td>
    <td align="right">53.92</td>
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
    <td align="right">68.75</td>
    <td align="right">103.33</td>
    <td align="right">20.37</td>
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
    <td align="right">2.1489</td>
    <td align="right">27.94</td>
    <td align="right">43.35</td>
    <td align="right">39.65</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">13.00</td>
    <td align="right">16.44</td>
    <td align="right">16.48</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">16.94</td>
    <td align="right">21.15</td>
    <td align="right">21.17</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">36.82</td>
    <td align="right">63.06</td>
    <td align="right">40.78</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">17.30</td>
    <td align="right">19.48</td>
    <td align="right">19.29</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">21.15</td>
    <td align="right">25.76</td>
    <td align="right">25.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">43.71</td>
    <td align="right">75.13</td>
    <td align="right">38.51</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">17.15</td>
    <td align="right">18.64</td>
    <td align="right">18.50</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">28.73</td>
    <td align="right">33.24</td>
    <td align="right">33.42</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">55.48</td>
    <td align="right">95.11</td>
    <td align="right">37.63</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">18.06</td>
    <td align="right">19.01</td>
    <td align="right">19.19</td>
    <td align="center">14</td>
    <td align="right">0.0158</td>
    <td align="right">35.57</td>
    <td align="right">37.65</td>
    <td align="right">38.51</td>
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
    <td align="right">2.7396</td>
    <td align="right">10.85</td>
    <td align="right">13.98</td>
    <td align="right">13.98</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">16.52</td>
    <td align="right">19.82</td>
    <td align="right">19.84</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">33.96</td>
    <td align="right">23.20</td>
    <td align="right">23.20</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">12.76</td>
    <td align="right">16.45</td>
    <td align="right">15.71</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">16.13</td>
    <td align="right">18.76</td>
    <td align="right">18.71</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">40.43</td>
    <td align="right">29.36</td>
    <td align="right">29.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">14.40</td>
    <td align="right">18.93</td>
    <td align="right">19.07</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">18.01</td>
    <td align="right">18.70</td>
    <td align="right">18.30</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">65.60</td>
    <td align="right">47.05</td>
    <td align="right">47.08</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0284</td>
    <td align="right">24.93</td>
    <td align="right">25.67</td>
    <td align="right">25.62</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">19.35</td>
    <td align="right">20.06</td>
    <td align="right">20.18</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">79.83</td>
    <td align="right">57.33</td>
    <td align="right">57.59</td>
  </tr>
</table>

<!--gcc-x86/comparison_table.cpp.txt-->

### Clang 18, x86
<!--clang-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">61.44</td>
    <td align="right">10.18</td>
    <td align="right">7.14</td>
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
    <td align="right">2.1546</td>
    <td align="right">13.69</td>
    <td align="right">22.55</td>
    <td align="right">26.60</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">9.46</td>
    <td align="right">12.32</td>
    <td align="right">12.33</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">12.64</td>
    <td align="right">16.00</td>
    <td align="right">16.00</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">19.34</td>
    <td align="right">34.93</td>
    <td align="right">29.06</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">11.91</td>
    <td align="right">14.03</td>
    <td align="right">14.01</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.25</td>
    <td align="right">22.42</td>
    <td align="right">22.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">24.75</td>
    <td align="right">47.09</td>
    <td align="right">29.84</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">13.63</td>
    <td align="right">15.32</td>
    <td align="right">15.33</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">23.88</td>
    <td align="right">31.94</td>
    <td align="right">31.97</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">32.28</td>
    <td align="right">59.97</td>
    <td align="right">30.14</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">14.48</td>
    <td align="right">16.26</td>
    <td align="right">16.54</td>
    <td align="center">14</td>
    <td align="right">0.0149</td>
    <td align="right">30.00</td>
    <td align="right">36.96</td>
    <td align="right">36.98</td>
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
    <td align="right">2.7635</td>
    <td align="right">6.95</td>
    <td align="right">9.22</td>
    <td align="right">9.25</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">11.67</td>
    <td align="right">13.82</td>
    <td align="right">13.76</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.12</td>
    <td align="right">16.60</td>
    <td align="right">16.50</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">11.56</td>
    <td align="right">13.90</td>
    <td align="right">13.92</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">13.59</td>
    <td align="right">15.21</td>
    <td align="right">15.21</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">17.68</td>
    <td align="right">22.27</td>
    <td align="right">22.25</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">13.61</td>
    <td align="right">17.52</td>
    <td align="right">17.52</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">14.53</td>
    <td align="right">16.66</td>
    <td align="right">16.64</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.37</td>
    <td align="right">30.66</td>
    <td align="right">30.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0297</td>
    <td align="right">17.09</td>
    <td align="right">21.86</td>
    <td align="right">21.88</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">15.81</td>
    <td align="right">17.76</td>
    <td align="right">17.75</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">32.91</td>
    <td align="right">35.64</td>
    <td align="right">35.67</td>
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
    <td align="right">72.53</td>
    <td align="right">41.86</td>
    <td align="right">9.82</td>
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
    <td align="right">2.1489</td>
    <td align="right">14.05</td>
    <td align="right">22.66</td>
    <td align="right">28.08</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">9.60</td>
    <td align="right">12.47</td>
    <td align="right">12.51</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">12.65</td>
    <td align="right">16.53</td>
    <td align="right">16.55</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">18.94</td>
    <td align="right">34.16</td>
    <td align="right">29.60</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">11.82</td>
    <td align="right">13.72</td>
    <td align="right">13.75</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">16.76</td>
    <td align="right">21.49</td>
    <td align="right">21.80</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">24.18</td>
    <td align="right">47.06</td>
    <td align="right">30.05</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">13.38</td>
    <td align="right">14.84</td>
    <td align="right">14.82</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">23.82</td>
    <td align="right">32.71</td>
    <td align="right">32.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">31.28</td>
    <td align="right">60.00</td>
    <td align="right">30.10</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">14.27</td>
    <td align="right">15.68</td>
    <td align="right">15.75</td>
    <td align="center">14</td>
    <td align="right">0.0158</td>
    <td align="right">29.81</td>
    <td align="right">36.73</td>
    <td align="right">36.63</td>
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
    <td align="right">2.7396</td>
    <td align="right">7.17</td>
    <td align="right">9.41</td>
    <td align="right">9.42</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">11.86</td>
    <td align="right">13.99</td>
    <td align="right">13.93</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.24</td>
    <td align="right">17.56</td>
    <td align="right">17.53</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">11.19</td>
    <td align="right">13.77</td>
    <td align="right">13.78</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">13.23</td>
    <td align="right">14.86</td>
    <td align="right">14.87</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">17.80</td>
    <td align="right">21.67</td>
    <td align="right">21.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">13.07</td>
    <td align="right">16.44</td>
    <td align="right">16.49</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">14.15</td>
    <td align="right">16.13</td>
    <td align="right">16.14</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">25.48</td>
    <td align="right">30.94</td>
    <td align="right">30.97</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0284</td>
    <td align="right">16.22</td>
    <td align="right">21.05</td>
    <td align="right">21.03</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">15.43</td>
    <td align="right">17.36</td>
    <td align="right">17.37</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">33.01</td>
    <td align="right">35.15</td>
    <td align="right">35.18</td>
  </tr>
</table>

<!--clang-x86/comparison_table.cpp.txt-->

### VS 2022, x86
<!--vs-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">42.01</td>
    <td align="right">8.58</td>
    <td align="right">6.63</td>
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
    <td align="right">2.1546</td>
    <td align="right">55.19</td>
    <td align="right">52.60</td>
    <td align="right">36.37</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">18.16</td>
    <td align="right">17.38</td>
    <td align="right">20.50</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">20.20</td>
    <td align="right">39.81</td>
    <td align="right">39.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">85.00</td>
    <td align="right">79.15</td>
    <td align="right">40.00</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">20.34</td>
    <td align="right">18.80</td>
    <td align="right">21.14</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">24.72</td>
    <td align="right">58.51</td>
    <td align="right">56.44</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">105.85</td>
    <td align="right">96.79</td>
    <td align="right">38.40</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">21.66</td>
    <td align="right">19.12</td>
    <td align="right">20.50</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">36.39</td>
    <td align="right">77.37</td>
    <td align="right">77.47</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">134.36</td>
    <td align="right">121.71</td>
    <td align="right">39.89</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">23.71</td>
    <td align="right">20.54</td>
    <td align="right">21.23</td>
    <td align="center">14</td>
    <td align="right">0.0149</td>
    <td align="right">41.95</td>
    <td align="right">92.72</td>
    <td align="right">92.82</td>
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
    <td align="right">2.7253</td>
    <td align="right">16.32</td>
    <td align="right">23.66</td>
    <td align="right">23.80</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">21.80</td>
    <td align="right">22.38</td>
    <td align="right">24.85</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">22.93</td>
    <td align="right">40.30</td>
    <td align="right">40.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5350</td>
    <td align="right">16.04</td>
    <td align="right">32.90</td>
    <td align="right">23.95</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">23.57</td>
    <td align="right">24.08</td>
    <td align="right">25.30</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">29.37</td>
    <td align="right">56.95</td>
    <td align="right">57.46</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1194</td>
    <td align="right">26.62</td>
    <td align="right">54.87</td>
    <td align="right">39.14</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">25.90</td>
    <td align="right">26.36</td>
    <td align="right">27.23</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">41.89</td>
    <td align="right">76.53</td>
    <td align="right">80.21</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0262</td>
    <td align="right">25.05</td>
    <td align="right">55.09</td>
    <td align="right">36.48</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">28.03</td>
    <td align="right">28.94</td>
    <td align="right">29.06</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">47.47</td>
    <td align="right">91.57</td>
    <td align="right">92.98</td>
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
    <td align="right">62.94</td>
    <td align="right">36.48</td>
    <td align="right">12.01</td>
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
    <td align="right">2.1489</td>
    <td align="right">62.40</td>
    <td align="right">56.67</td>
    <td align="right">40.45</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">19.66</td>
    <td align="right">18.01</td>
    <td align="right">22.45</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">22.34</td>
    <td align="right">40.61</td>
    <td align="right">40.65</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">98.03</td>
    <td align="right">90.06</td>
    <td align="right">44.56</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">22.73</td>
    <td align="right">19.45</td>
    <td align="right">22.13</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">27.34</td>
    <td align="right">62.13</td>
    <td align="right">60.88</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">139.03</td>
    <td align="right">144.55</td>
    <td align="right">46.11</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">28.44</td>
    <td align="right">24.61</td>
    <td align="right">25.18</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">42.69</td>
    <td align="right">82.54</td>
    <td align="right">82.78</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">244.87</td>
    <td align="right">207.55</td>
    <td align="right">55.80</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">40.86</td>
    <td align="right">32.67</td>
    <td align="right">34.31</td>
    <td align="center">14</td>
    <td align="right">0.0158</td>
    <td align="right">54.87</td>
    <td align="right">104.95</td>
    <td align="right">106.84</td>
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
    <td align="right">2.7254</td>
    <td align="right">17.02</td>
    <td align="right">28.91</td>
    <td align="right">28.94</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">24.07</td>
    <td align="right">24.98</td>
    <td align="right">28.37</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">25.64</td>
    <td align="right">41.64</td>
    <td align="right">41.82</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5375</td>
    <td align="right">17.88</td>
    <td align="right">40.55</td>
    <td align="right">30.98</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">27.76</td>
    <td align="right">27.78</td>
    <td align="right">30.44</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">36.54</td>
    <td align="right">63.58</td>
    <td align="right">65.96</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1187</td>
    <td align="right">35.95</td>
    <td align="right">80.13</td>
    <td align="right">59.83</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">35.66</td>
    <td align="right">37.91</td>
    <td align="right">36.51</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">51.64</td>
    <td align="right">83.70</td>
    <td align="right">87.35</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0287</td>
    <td align="right">41.58</td>
    <td align="right">90.14</td>
    <td align="right">70.26</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">44.04</td>
    <td align="right">48.61</td>
    <td align="right">48.92</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">62.64</td>
    <td align="right">106.05</td>
    <td align="right">108.63</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
